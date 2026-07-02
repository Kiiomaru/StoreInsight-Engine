from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from jinja2 import Environment, FileSystemLoader
from email.mime.application import MIMEApplication
import smtplib


class Email:
    def __init__(self):
        self.env = Environment(loader=FileSystemLoader("templates"))

    def config_email(self, remetente, destinatario, assunto):
        self.mail = MIMEMultipart()
        self.mail["From"] = remetente  # type: ignore
        self.mail["To"] = destinatario
        self.mail["Subject"] = assunto

    def montar_corpo(self, dados: dict):
        template = self.env.get_template("email_template.html")
        return template.render(**dados)

    def anexar_corpo(self, corpo):
        self.mail.attach(MIMEText(corpo, "html"))

    def anexar_arquivo(self, caminho_arquivo):
        with open(caminho_arquivo, "rb") as arquivo:
            anexo = MIMEApplication(arquivo.read())

        anexo.add_header(
            "Content-Disposition",
            "attachment",
            filename=caminho_arquivo.name,
        )
        self.mail.attach(anexo)

    def enviar_email(self, remetente, senha):
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(remetente, senha)  # type: ignore
            server.send_message(self.mail)  # type: ignore
