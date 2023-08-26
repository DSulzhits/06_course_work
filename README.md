# Mailing-List-service
Service for creating and managing mailing lists.
Includes 3 apps:
- mailing_list with models Client, MailingListMessage, MailingListLogs;
- users with model User;
- vlog with model Record.
CRUD realized for each model.
In mailing_list.services add code for sending emails to Users clients.
In users.services add code for sending email when new user registers or want to change password. Email send to users email specified at registration.
Front part of the project located in templates paths.

With this service authorised User can create and manage his own mailing lists for his clients, also User can create records and manage them. User can see another mailing lists, created by another users but can't manage or delete them.
