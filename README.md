# SDR-Lab2
Sisteme de Recomandare – UPB – Lab2  
Ivana Florin-Andrei – Master E-Guvernare – An I  

## DataSet Info  

**Nume:** Netflix Users Dataset  

**Sursă:** [Kaggle Link](https://www.kaggle.com/datasets/smayanj/netflix-users-database)

**Descriere:**  
Acest set de date conține informații despre un eșantion de **100 de utilizatori** ai unei platforme de tip Netflix.  
Fiecare utilizator este caracterizat prin informații demografice, preferințe de conținut și activitate recentă, utilizate pentru personalizarea recomandărilor.  

Acest dataset a fost folosit pentru a popula secțiunea **Users** din baza de date Recombee, definind proprietăți relevante pentru fiecare utilizator.  

**Fielduri disponibile:**  
- `User_ID` – identificator unic pentru fiecare utilizator  
- `Name` – numele complet al utilizatorului  
- `Age` – vârsta utilizatorului  
- `Country` – țara de proveniență  
- `Subscription_Type` – tipul de abonament (ex. *Basic*, *Standard*, *Premium*)  
- `Watch_Time_Hours` – numărul total de ore vizionate (activitate istorică)  
- `Favorite_Genre` – genul preferat (ex. *Drama*, *Action*, *Comedy*)  
- `Last_Login` – data ultimei autentificări (convertită la format timestamp pentru Recombee)  

---

## Integrare în Recombee  

- A fost creat un script Python (`load_users.py`) pentru încărcarea automată a utilizatorilor în Recombee.  
- Scriptul:
  - Definește proprietățile pentru entitatea **User** (`name`, `age`, `country`, `subscription_type`, `watch_time_hours`, `favorite_genre`, `last_login`)  
  - Citește fișierul `netflix_users.csv` cu ajutorul bibliotecii **pandas**  
  - Creează fiecare utilizator în Recombee (`AddUser`)  
  - Setează valorile corespunzătoare proprietăților (`SetUserValues`)  
  - Trimite datele în batch-uri către Recombee  

---

## Rezultat în Recombee  

După rularea scriptului:
- În **Catalog → Users** apar cei 100 de utilizatori încărcați din fișier  
- În **Catalog → Properties (Users)** sunt vizibile proprietățile definite  
- Fiecare utilizator conține valorile importate din CSV (vârstă, gen preferat, ore vizionate, etc.)  

---

## Legătura cu Lab1  

Acest laborator extinde munca din **SDR-Lab1**, în care au fost încărcate în Recombee item-urile (filmele și serialele Amazon Prime).  
În **Lab2**, a fost adăugată dimensiunea utilizatorilor, pregătind baza pentru următorul pas — **interacțiunile utilizator–item**, necesare pentru generarea de recomandări personalizate.  

