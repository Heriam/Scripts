#!/usr/bin/env python
from exchangelib import DELEGATE, Account, Credentials, Message, Mailbox, HTMLBody, Configuration, NTLM, EWSTimeZone, \
    EWSDateTime, DLMailbox
from exchangelib.protocol import BaseProtocol, NoVerifyHTTPAdapter
import urllib3, datetime, logging

# ----------- Logging --------------------

logging.basicConfig(
    level=logging.INFO,
    filemode="w",
    filename="log.txt",
    format="[%(asctime)s][%(levelname)s]:%(message)s"
)

# ----------- Variables --------------------

urllib3.disable_warnings()
TO_HAO_EMAIL = ['jiang.haoa@h3c.com']
TO_JINZHU_EMAIL = ['wangjinzhu@h3c.com']
TO_PL_EMAIL = ['&CTPL-ADNET-SEER-PL@h3c.com', '&RD-AI-Core@h3c.com']
TO_GROUP_EMAIL = ['&RD-AI-SA-Network@h3c.com', 'KF.xuezhetao@h3c.com']
EMAIL_FIELDS = ['mime_content', '_id', 'parent_folder_id', 'item_class', 'subject', 'sensitivity', 'text_body', 'body', 'attachments', 'datetime_received', 'size', 'categories', 'importance', 'in_reply_to', 'is_submitted', 'is_draft', 'is_from_me', 'is_resend', 'is_unmodified', 'headers', 'datetime_sent', 'datetime_created', 'reminder_due_by', 'reminder_is_set', 'reminder_minutes_before_start', 'display_cc', 'display_to', 'has_attachments', 'culture', 'effective_rights', 'last_modified_name', 'last_modified_time', 'is_associated', 'web_client_read_form_query_string', 'web_client_edit_form_query_string', 'conversation_id', 'unique_body', 'sender', 'to_recipients', 'cc_recipients', 'bcc_recipients', 'is_read_receipt_requested', 'is_delivery_receipt_requested', 'conversation_index', 'conversation_topic', 'author', 'message_id', 'is_read', 'is_response_requested', 'references', 'reply_to', 'received_by', 'received_representing']
GROUP_INCLUDE_EMAILS = {
    'xuezhetao kf8948 (Partner)': 'KF.xuezhetao@h3c.com'
}
GROUP_EXCLUDE_EMAILS = {
    'wangjinzhu (RD)': 'wangjinzhu@h3c.com'
}


class EmailBox:
    SENDER = 'jiang.haoa@h3c.com'
    SENDER_NAME = ''
    BaseProtocol.HTTP_ADAPTER_CLS = NoVerifyHTTPAdapter
    tz = EWSTimeZone.localzone()
    creds = Credentials(
        username='j16492',
        password='Jh203142'
    )
    config = Configuration(server='rndcas.h3c.com', credentials=creds, auth_type=NTLM)
    account = Account(
        primary_smtp_address=SENDER,
        config=config,
        autodiscover=False,
        access_type=DELEGATE
    )

    def send_email(self, to, subject, body, cc=[]):
        m = Message(
            account=self.account,
            subject=subject,
            body=HTMLBody(body),
            to_recipients=[Mailbox(email_address=email) for email in to],
            cc_recipients=[Mailbox(email_address=email) for email in cc]
        )
        m.send_and_save()

    def search_reports_of_date_range(self, dateRange=None):
        if not dateRange:
            start = datetime.datetime.now() - datetime.timedelta(days=1)
            end = datetime.datetime.now() + datetime.timedelta(days=1)
        else:
            start, end = dateRange
        folder = self.account.root / '信息存储顶部' / '日报' / '组内日报'
        return folder.filter(datetime_received__range=(self.tz.localize(EWSDateTime(start.year, start.month, start.day)), self.tz.localize(EWSDateTime(end.year, end.month, end.day))))

    def remind_report_absent_member(self):
        exclude_emails = [msg.sender.email_address for msg in self.search_reports_of_date_range()] + TO_HAO_EMAIL
        if 2 <= datetime.datetime.now().isoweekday() <= 6 and len(exclude_emails) > 3:
            subject = '[温馨提醒]请记得发日报'
            body = '程序未检测到你昨天发的日报，每天工作结束请及时汇报当天工作进展。若有请假或者其他特殊情况可忽略。'
            for to in [email for email in self.get_member_email_address_map().values() if email not in exclude_emails]:
                self.send_email([to],subject,body,TO_HAO_EMAIL)
                logging.info('Sent report reminder to %s' % to)

    def get_member_email_address_map(self):
        map = {}
        for mailbox in self.account.protocol.expand_dl(DLMailbox(email_address='&RD-AI-SA-Network', mailbox_type='PublicDL')):
            if mailbox.email_address not in GROUP_EXCLUDE_EMAILS.values():
                map[mailbox.name] = mailbox.email_address
        for name, email in GROUP_INCLUDE_EMAILS.items():
            map[name] = email
        return map

    def find_email_address_by_name(self, name):
        for key, email in self.get_member_email_address_map().items():
            if name.split(' ')[0] == key.split(' ')[0]:
                return email
