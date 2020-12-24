from subprocess import call

call('sudo update-ca-certificates --fresh', shell=True)
call('export SSL_CERT_DIR=/etc/ssl/certs', shell=True)
