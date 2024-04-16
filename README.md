# MedEZ

### Problem Statement

In today's world, people face the issue of having to compare prices of medicines in their prescriptions across various online platforms, which can be a hectic task especially when dealing with multiple medications. This problem becomes even more significant when expensive medications need to be purchased, as it could result in potential savings of up to 80% in some cases. From identifying the names of the medications in a prescription to actually purchasing them from an online pharmacy and keeping track of their dosage, the process can be overwhelming for a patient, and there is a need to simplify it.

### Solution

- Our solution aims to simplify the process of purchasing and managing medications for patients by integrating various technologies. We will use **Optical Character Recognition (OCR)** to extract medication details from prescriptions using **Google Cloud Vision**. We will then employ the Med7 **machine learning model** from **spaCy** to extract the medication names, dosages, and frequencies.

- To ensure efficient retrieval and management of data, we will cache the extracted medication details and prices in a database. The backend, written in Python, will handle data processing, price comparisons, and medication scheduling using multi-threading to optimize performance. We will use **web scraping techniques** to fetch medication prices from various online pharmacies.

- For the frontend, we will develop a **React-based user interface** that will showcase medication details, including names, dosages, durations, and prices from various websites. Additionally, the frontend will feature a calendar where patients can schedule medication reminders and track their dosages. The calendar will be integrated with **Google Calendar**, allowing patients to receive reminders across devices and platforms.

- Our solution aims to simplify the medication purchasing process for patients, provide them with valuable cost-saving opportunities, and ensure that they can easily track and manage their medication schedules.

### Methodology:

![Flow Chart](/assets/flow.png?raw=true)

### Tech Stack:

- Flask
- React
- Node
- MongoDB
- Python
- Google Cloud Vision API
- Med7 NLP Model

### Results:

_Search results for Crocin:_
<br/><br/>
![Crocin](</screenshots/Screenshot (06).png?raw=true>)
<br/><br/>
_Search results for Diamox:_
<br/><br/>
![Diamox](</screenshots/Screenshot (07).png?raw=true>)
<br/><br/>
_Showcasing alternatives:_
<br/><br/>
![Alternatives](</screenshots/Screenshot (08).png?raw=true>)
<br/><br/>
_Sample prescription:_
<br/><br/>
![Sample Prescription](/screenshots/prescription.jpeg?raw=true)
<br/><br/>
_Prescription OCR:_
<br/><br/>
![Prescription OCR](</screenshots/Screenshot (09).png?raw=true>)
<br/><br/>

### Installation steps:

To install the application, follow these steps:

```
git clone https://github.com/souravgupta0401/MedEZ/
```

```
cd MedEZ
```

**Sample format for server/.env:**

```bash
DB_URL = mongodb+srv://user:password@cluster0.xxxxxxxx.mongodb.net/
JWT_SECRET = ThisIsMyJWT_SECRET
JWT_LIFETIME = 10d
CLIENT_ID = xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx.apps.googleusercontent.com
CLIENT_SECRET = xxxxxxxxxxxxxxxxxxxxxxxxxx
# Uncomment if running on remote
# REDIRECT_URI = http://example.com
```

**Sample format for client/.env:**

```bash
REACT_APP_CLIENT_ID =  xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx.apps.googleusercontent.com
REACT_APP_CLIENT_SECRET = xxxxxxxxxxxxxxxxxxxxxxxxxx
# Uncomment if running on local machine
# REACT_APP_HOSTNAME = http://localhost:8080
```

- ### Development Mode

  #### Flask Endpoint:

  ```
  cd flask_server
  ```

  ```
  pip install -r requirements.txt
  ```

  ```
  flask run
  ```

  #### React Endpoint:

  ```
  cd client
  ```

  ```
  npm install
  ```

  ```
  npm start
  ```

  #### NodeJS Endpoint:

  ```
  cd server
  ```

  ```
  npm install
  ```

  ```
  npm start
  ```

  - The React Frontend will be hosted at port 3000
  - The Flask Backend will be hosted at port 5000
  - The NodeJS Backend will be hosted at port 8080

- ### Production Mode

  #### Nginx Configuration:

  ```
  sudo apt install nginx
  ```

  ```
  nano /etc/nginx/sites-available/default
  ```

  ```
  server {
    listen 80;
    server_name example.com;

    root /var/www/html;
    index index.html index.htm;
    try_files $uri /index.html;
    location / {
        try_files $uri $uri/ = 404;
    }
  }
  server {
      listen 80;
      server_name flaskapi.example.com;
      location / {
                  include proxy_params;
                  proxy_pass http://localhost:5000;
      }
  }
  server {
      listen 80;
      server_name api.example.com;
      location / {
          proxy_set_header Host $host;
          proxy_pass http://localhost:8080;
          proxy_redirect off;
          proxy_buffering off;
          proxy_set_header X-Real-IP $remote_addr;
          proxy_set_header X-Forwarded-Host $host;
          proxy_set_header X-Forwarded-Port $server_port;
      }
  }
  ```

  ```
  systemctl restart nginx
  ```

  #### React Endpoint:

  ```
  cd client
  ```

  ```
  npm install
  ```

  ```
  npm run build
  ```

  ```
  mv build/* /var/www/html
  ```

  #### NodeJS Endpoint:

  ```
  cd server
  ```

  ```
  npm install
  ```

  ```
  npm install pm2 -g
  ```

  ```
  pm2 start index.js -i max
  ```

  #### Flask Endpoint:

  ```
  cd flask_server
  ```

  ```
  pip install -r requirements.txt
  ```

  ```
  pip install gunicorn
  ```

  ```
  nano /etc/systemd/system/flaskapi.service
  ```

  ```
  [Unit]
  Description=Gunicorn instance to serve Flask
  After=network.target
  [Service]
  User=ubuntu
  Group=ubuntu
  WorkingDirectory=/home/ubuntu/MedEZ/flask_server/
  ExecStart=gunicorn --bind 0.0.0.0:5000 --workers 4 app:app
  [Install]
  WantedBy=multi-user.target
  ```

  ```
  sudo systemctl start flaskapi
  ```

  ```
  sudo systemctl enable flaskapi
  ```

  - The React Frontend will be hosted at _example.com_
  - The Flask Backend will be hosted at _flaskapi.example.com_
  - The NodeJS Backend will be hosted at _api.example.com_
