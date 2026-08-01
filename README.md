# Resume Builder


Resume Builder is a Django-based web application that allows users to create, manage, and preview resumes through a simple web interface.


## Project Description


This project helps users build resumes by entering their personal, educational, professional, and skill related details. Users can create resumes, view saved resumes from the dashboard, and preview the latest resume in a clean A4-style layout before saving or printing it.

The application includes user authentication, resume creation, resume management, and a responsive resume preview page.



## Features



- User signup and login

- User dashboard

- Create resume

- Edit resume

- View saved resumes

- Preview latest resume

- Clean A4-style resume preview

- Print-friendly resume layout

- User-specific resume records

- Responsive user interface



## Technologies Used



- Python

- Django

- HTML

- CSS

- Bootstrap

- JavaScript

- SQLite



## Main Modules



### Authentication



Users can create an account, log in, and access their own resume dashboard.



### Dashboard



The dashboard displays resumes created by the logged-in user and provides options to create, edit, and preview resumes.



### Resume Form



The resume form collects details such as personal information, education, experience, skills, projects, and other resume sections.



### Resume Preview



The preview page allows users to review their latest resume in a clean A4 layout before saving or printing it. If no resume exists, the page shows a Create First Resume option.



## Project Structure



```text

resume\_project/

├── builder/

│   ├── templates/

│   │   └── builder/

│   ├── urls.py

│   ├── views.py

│   ├── models.py

│   ├── forms.py

│   └── apps.py

├── resume\_project/

│   ├── settings.py

│   ├── urls.py

│   ├── asgi.py

│   └── wsgi.py

├── manage.py

├── requirements.txt

├── .gitignore

└── README.md

```



## How to Run



```bash

git clone https://github.com/TavishaBudhiraja/ResumeBuilder.git

cd resume-builder

python -m venv r1

r1\Scripts\activate

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver

```



Open in browser:



```text

http://127.0.0.1:8000/

```



## Application URLs



| Page | URL |

|---|---|

| Dashboard | `/` |

| Login | `/login/` |

| Signup | `/signup/` |

| Create Resume | `/create-resume/` |

| Resume Form | `/resume-form/` |

| Resume Preview | Available from dashboard after creating a resume |



## How to Use



Create an account, log in, create a resume, view it from the dashboard, and preview it in an A4-style layout before saving or printing.





## Author



TAVISHA BUDHIRAJA

