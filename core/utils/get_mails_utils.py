import email
import html
import imaplib
from email.header import decode_header
from email.utils import parseaddr
from traceback import format_exc

from bs4 import BeautifulSoup

from core.logger import logger


def clean_content_html(content_html) -> str:
    soup = BeautifulSoup(content_html, "html.parser")

    text_cleaned = soup.get_text(separator=" ", strip=True)

    text_cleaned = html.unescape(text_cleaned)

    return text_cleaned


class EmailProcessor:
    def __init__(self, server, username, password):
        self.server = server
        self.username = username
        self.password = password
        self.mail = None

    def connect(self):
        try:
            self.mail = imaplib.IMAP4_SSL(host=self.server)
            self.mail.login(user=self.username, password=self.password)
            status, _ = self.mail.noop()
            if status != "OK":
                logger(
                    level_name="ERROR",
                    message="Falha na conexão IMAP.",
                    extra={"method": "get_mails_task"},
                )
                return False
            return True
        except imaplib.IMAP4.error as e:
            logger(
                level_name="ERROR",
                message=f"Erro ao conectar: {e}",
                extra={"method": "get_mails_task"},
            )
            return False

    def fetch_unseen_emails(self):
        self.mail.select(mailbox="inbox")
        status, messages = self.mail.search(None, "UNSEEN")
        if status == "OK":
            return messages[0].split()
        return []

    def fetch_email(self, num):
        status, msg_data = self.mail.fetch(message_set=num, message_parts="(RFC822)")
        if status == "OK":
            return email.message_from_bytes(msg_data[0][1])
        return None

    def mark_as_seen(self, num):
        self.mail.store(message_set=num, command="+FLAGS", flags="\\Seen")

    def logout(self):
        self.mail.logout()


class EmailDecoder:
    @staticmethod
    def decode_subject(msg):
        subject, encoding = decode_header(header=msg["Subject"])[0]
        if isinstance(subject, bytes):
            subject = subject.decode(encoding=encoding if encoding else "utf-8")
        return subject

    @staticmethod
    def get_sender_info(msg):
        from_ = msg.get("From")
        if from_:
            return parseaddr(from_)
        return "", ""

    @staticmethod
    def get_body(message):
        """Retrieve the body content of an email message."""
        body = ""
        if message.is_multipart():
            for part in message.walk():
                if part.get_content_type() in ("text/plain", "text/html"):
                    body = EmailDecoder.decode_payload(part=part)
                    if body:
                        break
        else:
            body = EmailDecoder.decode_payload(part=message)
        return body

    @staticmethod
    def decode_payload(part):
        """Decode the payload of a message part."""
        try:
            return part.get_payload(decode=True).decode()
        except UnicodeDecodeError:
            return part.get_payload(decode=True).decode("iso-8859-1")
        except Exception as err:
            logger(
                level_name="ERROR",
                message="Erro ao decodificar a mensagem",
                extra={
                    "method": "get_mails_task",
                    "message_error": str(object=err),
                    "error": format_exc(),
                },
            )
            return ""

    @staticmethod
    def clean_body(body):
        try:
            return clean_content_html(content_html=body)
        except Exception:
            return body


# @shared_task
def get_mails_task():
    server = "imappro.zoho.com"
    username = "jhonatan.rian@govone.digital"
    password = "J1f5e3o#mily@0543"

    email_processor = EmailProcessor(
        server=server, username=username, password=password
    )
    if not email_processor.connect():
        return

    messages = email_processor.fetch_unseen_emails()
    # for num in messages:
    #     msg = email_processor.fetch_email(num=num)
    #     if msg:
    #         subject = EmailProcessor.decode_subject(msg=msg)
    #         from_name, from_email = EmailDecoder.get_sender_info(msg=msg)
    #         body = EmailDecoder.get_body(message=msg)
    #         content = EmailDecoder.clean_body(body=body)
    #
    #         email_processor.mark_as_seen(num=num)


    email_processor.logout()
