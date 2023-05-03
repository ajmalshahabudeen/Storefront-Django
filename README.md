# Storefront-Django
E-commerce App - Django

--- Using Demo SMTP server ---
To setup smtp4dev run this in terminal:
docker run --rm -it -p 3000:80 -p 2525:25 rnwood/smtp4dev


--- Using Redis for Message Broker + Cache ---
To setup Redis run this in terminal:
docker run -d -p 6379:6379 redis