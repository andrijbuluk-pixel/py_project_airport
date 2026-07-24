### Airport API
Airport API service for managing flights, tickets, planes and airports.

### Main features:
registration/authentication (JWT),

ordering tickets for a specific person,

managing employees,

managing flight routes,

aircraft management (adding their photo and description),

CRUD system is implemented for all models.

Technologies
Python, Django, DRF, PostgreSQL, Docker.

### API endpoints:
/api/airport/crew/ - employees,

/api/airport/type/ - flight types,

/api/airport/airplane/ - description of the plane,

/api/airport/airport/ - airport,

/api/airport/route/ - routes,

/api/airport/flight/ - flight,

/api/airport/order/ - order,

/api/airport/ticket/ - ticket,

### Example of requests:
To register a user, go to the link - **/api/user/register/** and pass the username and password. After registering **/api/user/token/**, enter your data, receive the token **/api/doc/swagger/** for convenience, click on the green AUTHORIZE button and enter the assigned access token in the Bearer field and AUTHORIZE -
Close you have a simple user ready, he can view the data to create an admin, you just need to lead
**docker-compose exec airport python manage.py createsuperuser**
The end

Instructions for local startup.
Cloning **git clone**

Creation and activation of **venv .**

Install dependencies **pip install -r requirements.txt**

Run migration **python manage.py migrate**

Run the server **python manage.py runserver**

### Running via Docker:
Building the container and running **docker-compose up --build**


### Diagram
<img width="753" height="681" alt="Airport" src="https://github.com/user-attachments/assets/147b0130-b346-42ba-b58a-bd861f6c112a" />

<img width="710" height="676" alt="Знімок екрана 2026-07-24 175042" src="https://github.com/user-attachments/assets/2441c21e-2817-4133-901f-e5271e77aceb" />
<img width="478" height="532" alt="Знімок екрана 2026-07-24 175129" src="https://github.com/user-attachments/assets/ff4ff043-8586-4a2f-bc70-4d5276a4aa68" />
<img width="713" height="563" alt="Знімок екрана 2026-07-24 175143" src="https://github.com/user-attachments/assets/6331e2fe-c787-45a9-bba3-1c0eca74ca79" />
<img width="731" height="621" alt="Знімок екрана 2026-07-24 175208" src="https://github.com/user-attachments/assets/b0cf5d12-e542-4fc3-b108-e6c0066aeb16" />
<img width="711" height="605" alt="Знімок екрана 2026-07-24 175233" src="https://github.com/user-attachments/assets/041559d0-1e15-4ccf-8778-dd07145a9ac8" />
<img width="728" height="530" alt="Знімок екрана 2026-07-24 175258" src="https://github.com/user-attachments/assets/977e5f2b-60da-446d-a20b-47e8ea161dcc" />
<img width="712" height="610" alt="Знімок екрана 2026-07-24 175336" src="https://github.com/user-attachments/assets/98439873-a954-423f-a25e-e04f4971c1da" />
<img width="723" height="595" alt="Знімок екрана 2026-07-24 175353" src="https://github.com/user-attachments/assets/e556f2d0-0994-4d7e-836a-fe0a6ee4c0c9" />
<img width="720" height="621" alt="Знімок екрана 2026-07-24 175548" src="https://github.com/user-attachments/assets/ace5e386-af5e-4492-b4a5-3c301e900771" />
<img width="747" height="500" alt="Знімок екрана 2026-07-24 175559" src="https://github.com/user-attachments/assets/d41bfd95-1804-4f47-b2da-2e7e963441e3" />
<img width="731" height="692" alt="Знімок екрана 2026-07-24 175645" src="https://github.com/user-attachments/assets/0cf75387-8dfc-441a-bf92-047747215c48" />
<img width="712" height="601" alt="Знімок екрана 2026-07-24 175707" src="https://github.com/user-attachments/assets/363018b9-e285-4495-895e-1ad649257396" />
<img width="753" height="532" alt="Знімок екрана 2026-07-24 175715" src="https://github.com/user-attachments/assets/24f30be9-f4a9-432e-b8be-82c8b495a654" />
<img width="710" height="637" alt="Знімок екрана 2026-07-24 175739" src="https://github.com/user-attachments/assets/53932ec5-ac0b-4977-989d-fb019ccd7005" />
<img width="733" height="513" alt="Знімок екрана 2026-07-24 175747" src="https://github.com/user-attachments/assets/5c8b3836-7024-492c-bfaf-311c2f6717ea" />
<img width="750" height="617" alt="Знімок екрана 2026-07-24 175759" src="https://github.com/user-attachments/assets/60d4f44f-8d05-49bf-8419-ad55273ef4af" />
<img width="737" height="588" alt="Знімок екрана 2026-07-24 175814" src="https://github.com/user-attachments/assets/82414b83-1b71-4b21-811b-d425ea8c2795" />
#User
<img width="1321" height="552" alt="Знімок екрана 2026-07-24 092754" src="https://github.com/user-attachments/assets/1dfba1d7-4b00-460d-9d94-fa52d98d123b" />
<img width="1112" height="698" alt="Знімок екрана 2026-07-24 173634" src="https://github.com/user-attachments/assets/3bec511f-d208-4ac4-96d9-fab7404bfd4a" />
<img width="1008" height="667" alt="Знімок екрана 2026-07-24 173641" src="https://github.com/user-attachments/assets/3dc789d7-8219-463a-9492-edb52bf3942c" />
<img width="947" height="691" alt="Знімок екрана 2026-07-24 173656" src="https://github.com/user-attachments/assets/958f8334-df7c-4282-8a74-d0280b64e4bd" />
<img width="1037" height="700" alt="Знімок екрана 2026-07-24 173751" src="https://github.com/user-attachments/assets/8a192c32-9e91-4b6b-841d-45ff96c65665" />
<img width="923" height="697" alt="Знімок екрана 2026-07-24 173807" src="https://github.com/user-attachments/assets/b399e7bc-05c7-4924-9979-c32964b288fb" />




