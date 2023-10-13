
## API Documentation

There is a Postman collection that details all of the API endpoints within the project.

## Service Delivery

To deliver a Django REST application to end users, follow these steps: Choose a hosting environment (e.g., Heroku, AWS, or DigitalOcean), set up a server or use a Platform-as-a-Service (PaaS) if needed, prepare your application for production, use Git for version control, collect static files, configure your database and set up environment variables, set up a web server (Nginx or Apache) as a reverse proxy, configure your domain and DNS settings, apply database migrations, manage secrets using environment variables, establish firewall and security measures, conduct testing in the production environment, and consider deployment automation and CI/CD pipelines. To monitor the service and streamline maintenance, implement monitoring and logging tools, consider scaling for growth, and ensure regular updates. Popular tools used for this process include Git for version control, Nginx or Apache as web servers, Let's Encrypt for HTTPS, and Fabric or Ansible for deployment automation. By following these steps and using the mentioned tools, you can successfully deliver the Movie Rating Django REST application to end users while ensuring security and scalability.

## Future Changes

Due to the time constraints, I didn't get around to implementing Audit trails for users. In order to do this, I would create an AuditLog model tracking the user action and timestamp. I would then use signals in Django to track if anything was updated, created, or deleted, saving who made the change and at what time to the new table.

## Use of ChatGPT

Chat GPT was not used during development, as I find it often gets code wrong, which takes longer to debug over just writing code myself. Chat GPT was used during the creation of this document as it allowed quick summarization and idea generation for how this service could be delivered. It also allowed for corrections in grammar and spelling. 
