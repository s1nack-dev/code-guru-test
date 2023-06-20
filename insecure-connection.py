def ftp_connection_noncompliant():

    import ftplib

    # Noncompliant: insecure ftp used.

    cnx = ftplib.FTP("ftp://anonymous@example.com")
