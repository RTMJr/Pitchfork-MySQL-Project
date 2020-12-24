from subprocess import call

# generate fresh certificates for ssl certificate verification
# prevents URLError
call('sudo update-ca-certificates --fresh', shell=True)
call('export SSL_CERT_DIR=/etc/ssl/certs', shell=True)
