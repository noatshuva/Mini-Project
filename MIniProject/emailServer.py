from __future__ import annotations
import os.path
import urllib.request
import puremagic
import re
import smtpd
import email
from typing import Any
import suspicious


class emailServer(smtpd.SMTPServer):

    def process_message(self, peer, mailfrom: str, rcpttos: list[str], data: bytes | str, **kwargs: Any) -> str | None:

        content = email.message_from_string(data.decode("utf-8"))

        for msg in content.walk():
            if msg.get_content_maintype() == 'multipart':
                continue

            if msg.get_filename():
                # check file name
                if re.search("virus", msg.get_filename(), re.IGNORECASE) is not None \
                        or re.search("spam", msg.get_filename(), re.IGNORECASE) is not None:
                    print("WARNING: This file contains a suspicious name")
                    return

                # check that file name type equals file type
                if os.path.splitext(msg.get_filename())[1] != puremagic.from_file(msg.get_filename()):
                    print("WARNING: File name type is different from file type")
                    print(f"File name type: {os.path.splitext(msg.get_filename())[1]} "
                          f"File type: {puremagic.from_file(msg.get_filename())}")
                    return

            # check signature
            virus_list = suspicious.virus_list_from_file("Files/VirusSignatures")
            for v in virus_list:
                if v.signature in msg.get_payload(decode=True):
                    # throw a warning
                    print("WARNING: This file contains a signature virus")
                    return

            # check url
            try:
                playload = msg.get_payload(decode=True).decode("utf-8")
                url_list = re.findall(r'(https?://[^\s]+)', playload)
                for url in url_list:
                    redirect = urllib.request.urlopen(url).geturl()
                    if redirect != url:
                        print("WARNING: This file contains a redirect URL")
                        print(f"URL name: {url} URL redirect: {redirect}")
                        return
            except:
                continue
        print("Mail is clean :)")
        return
