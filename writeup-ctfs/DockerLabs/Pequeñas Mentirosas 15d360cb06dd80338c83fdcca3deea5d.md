# Pequeñas Mentirosas

Plataforma: Dockerlabs
OS: Linux
Level: Easy
Status: In progress
Complete: No
Created time: 15 de diciembre de 2024 16:08

## Recopilación de información

<aside>
💡 Empezamos con el reconocimiento de la maquina

</aside>

### **Escaneo de puertos**

Comenzamos con un escaneo para identificar que puertos están abiertos.

---

Scaneo inicial

```bash
❯ sudo nmap -p- --open -T5 -sS --min-rate 5000 -vvv -n -Pn 10.88.0.2 -oG targeted
```

![image.png](<imagenes/image 95.png>)

Scaneo profundo

```bash
❯ sudo nmap -p22,80 -sCV 10.88.0.2 -vvv -oN allports
```

![image.png](<imagenes/image 96.png>)

### **Enumeración de servicios**

Una vez listado los puertos accesibles, procederemos a realizar la enumeración de servicios para su posterior identificación de vulnerabilidades.

---

- **Identificación de vulnerabilidades**
    - 22 : OpenSSH 9.2p1 Debian 2+deb12u3 (protocol 2.0)
    - 80 : http    Apache httpd 2.4.62 (Debian)
    
- **Enumeración Web**
    
    ```bash
    ❯ nmap --script=http-enum -sV -p80 10.88.0.2
    nmap -p 80 --script http-title,http-headers,http-methods,http-enum target-ip
    ```
    
    No muestra nada. Miramos la web
    
    ![image.png](<imagenes/image 97.png>)
    
    Hacemos fuzzing con gobuster:
    
    ```bash
    ❯ gobuster dir -u http://10.88.0.2 -w /usr/share/seclists/Discovery/Web-Content/directory-list-2.3-medium.txt
    ```
    
    No encontramos nada
    
    Probamos con whatweb:
    
    ```bash
    whatweb 10.88.0.2
    http://10.88.0.2 [200 OK] Apache[2.4.62], Country[RESERVED][ZZ], HTTPServer[Debian Linux][Apache/2.4.62 (Debian)], IP[10.88.0.2]
    ```
    

Al no encontrar nada , probamos con la pista y buscamos password para el usuari a con hydra

```bash
❯ hydra -l a -P /usr/share/wordlists/rockyou.txt.gz 10.88.0.2 ssh
```

![image.png](<imagenes/image 98.png>)

## Explotación

<aside>
💡

</aside>

### Explotación 1

### Explotación 2

### Explotación 3

## Explotación posterior

<aside>
💡

</aside>

### Escalada de privilegios

## Conclusión

<aside>
💡 En esta sección, debes proporcionar un resumen de la máquina para cuando tengas que volver a ella, puedas saber conocer de forma rápida de que se trataba

</aside>