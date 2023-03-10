Steps to install webserver 

1. Create an Ansible playbook to install and configure the web server:
Code Added in web-server.yml

This playbook installs Nginx, copies the index.html file to the default web root directory, and starts the Nginx service.

2. Create a self-signed SSL/TLS certificate for the web server

openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/ssl/private/nginx-selfsigned.key -out /etc/ssl/certs/nginx-selfsigned.crt

This command generates a self-signed SSL/TLS certificate and private key and saves them in the specified locations.

3. Add the Ansible playbook to configure SSL/TLS to same web-server.yml

4. Create a test playbook to validate the server configuration:
Added Ansible playbook in test-web-server.yml
This playbook checks the status of the Nginx service and verifies that it is running.

5. Run the playbooks to deploy and test the web server:
ansible-playbook web-server.yml
ansible-playbook test-web-server.yml

These commands run the web-server.yml playbook to deploy the web server, and the test-web-server.yml playbook to test the server configuration.

After these steps, your web server should be deployed and secured with SSL/TLS, and the server configuration should be validated by the automated tests

