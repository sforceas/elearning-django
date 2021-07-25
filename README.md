# Django E-Learning Platform

# Software Requirements

## Table of contents
[1. Purpose](#1-purpose)<br>
[2. Scope](#2-scope)<br>
[3. References](#3-references)<br>
[4. Functionalities](#4-functionalities)<br>
[5. Types and characteristics of users](#5-types-and-characteristics-of-users)<br>
[6. Production enviornment](#6-poduction-enviornment)<br>
[7 Functional requirements](#7-functional-requirements)<br>
[8. Purpose](#8-bussiness-rules)<br>
[9. Interface requirements](#9-interface-requirements)<br>
[10. Non functional requirements](#10-non-functional-requirements)<br>
[11. Other requirements](#11-other-requirements)<br>
[12. Glossary](#12-glossary)<br>


## 1. Purpose

En esta sección se define el nombre o título del software que se está especificado en el documento, incluyendo su número de versión o Release.

Luego se describe cuales componentes o partes del alcance del producto están incluidas en el documento, estableciendo si este documento cubre la totalidad del software, sólo una parte del sistema, subsistema o subgrupo de procesos.


## 2. Scope

Se incluye una corta descripción del alcance del software que se está especificando, incluyendo:

•	Su propósito u objetivo general.
•	Beneficios que brinda al área de negocio y organización.
•	Objetivos y metas. Es recomendable establecer la relación de los objetivos del software con los objetivos corporativos y estrategias de negocio.
•	Se puede hacer referencia a otros documentos, por ejemplo una definición de alcance u acta de constitución del proyecto.

## 3. References

[1] [A Smart Way to Build Skills – An E-Learning Portal Data Model](https://vertabelo.com/blog/a-smart-way-to-build-skills-an-e-learning-portal-data-model/). Author: Shantanu Kher. Source:Vertabelo.<br>
[2] [Heroku. Getting stardet with python](https://devcenter.heroku.com/articles/getting-started-with-python). Source:Heroku.<br>

## 4. Functionalities

Lista de las funcionalidades del software que se están especificando en el documento de requerimientos. Cada funcionalidad puede estar compuesta por uno o varios requerimientos funcionales de software.

Aquí solo se incluye una lista numerada de las principales funcionalidades, la información detallada de requerimientos funcionales se documenta en la sección 7 de este documento.

## 5. Types and characteristics of users

En esta sección se clasifican los usuarios que utilizaran el producto. La clasificación puede ser en función a la frecuencia de uso, grupo de funcionalidades utilizadas, privilegios de seguridad, nivel de experiencia y otros parámetros.

Se puede usar una lista para enumerar los usuarios tipo que utilizarán el software, describiendo las características de cada uno.

Para cada tipo de usuario, se pueden mencionar las funcionalidades de producto (Sección 4) que le sean relevantes. Igualmente se puede hacer mención de cuales usuarios utilizan una mayor parte del sistema y con más frecuencia, para distinguirlos de usuarios ocasionales o que acceden a pocas funcionalidades.


## 6. Poduction enviornment
The app is deployed in Heroku. 


## 7. Functional requirements

Functional requirementes of the application are described on the requirement traceability matrix.

|ID   	|Description  	|Source   	|Justification   	    |Release   	            |Test strategy  |UAT            |Status |Active |Flag   |Comments
|---	|---	        |---        |---	                |---	                |---	        |---            |---    |---    |---    |---
|1   	|   	        |           |   	                |      	                |   	        |               |       |       |       |
|2  	|   	        |           |   	                |      	                |   	        |               |       |       |       |
|3  	|   	        |           |   	                |      	                |   	        |               |       |       |       |
|4  	|   	        |           |   	                |      	                |   	        |               |       |       |       |
|5  	|   	        |           |   	                |      	                |   	        |               |       |       |       |
|6  	|   	        |           |   	                |      	                |   	        |               |       |       |       |
|7  	|   	        |           |   	                |      	                |   	        |               |       |       |       |
|8  	|   	        |           |   	                |      	                |   	        |               |       |       |       |
|9  	|   	        |           |   	                |      	                |   	        |               |       |       |       |
|10  	|   	        |           |   	                |      	                |   	        |               |       |       |       |


## 8. Bussiness rules
Listado de reglas y principios que aplican a todo el conjunto de requerimientos de software contenidos en el documento. Un ejemplo es cuales individuos o roles pueden desempeñar cierta función bajo ciertas circunstancias.
Para hacer cumplir las reglas de negocio, podría ser necesaria la definición de requerimientos funcionales que aplican a todo el sistema, no a una funcionalidad especifica.

## 9. Interface requirements

### 9.1. User interfaces
Aquí se describen las características de cada interfaz con el usuario. 
* Se pueden clasificar por tipos o áreas del sistema con interfaz distinta.
* Pueden incluirse ejemplos de pantallas.
* Describir los estándares de interfaz gráfica (GUI).
* Guías de estilo sobre organización de pantalla, estándares para botones, funciones que se mostrarán en todas las pantallas.


### 9.2. Hardware interfaces
Información sobre cuales tipos de dispositivos soporta el sistema por ejemplo: Computadores, dispositivos móviles, impresoras, otros dispositivos.
Protocolos de comunicación que soporta.
Interacciones de datos y control entre el software y el hardware.

### 9.3 Software interfaces
The software interface is defined by the deployment platform (Heroku). There are two avaiable software interfaces:
* Heroku client: Runs on local shell (recomended). Documentation in [2](#3-references).
* Heroku dashboard: Runs on web browser on https://dashboard.heroku.com/.


### 9.4. Comunication interfaces
Requerimientos de las funciones de comunicación que requiere el producto, incluyendo email, navegadores web, protocolos de comunicación de red, formularios electrónicos, entre otros.
Incluye formatos de mensajería, estándares de comunicación (Ej. FTP, HTTP, etc.). Describir también requerimientos de encriptación y seguridad en las comunicaciones.


## 10. Non functional requirements
Los requerimientos no funcionales son los que especifican criterios para evaluar la operación de un servicio de tecnología de información, en contraste con los requerimientos funcionales que especifican los comportamientos específicos.
Para ver algunos ejemplos de cómo se redactan los requerimientos no funcionales, te recomendamos el siguiente enlace:


## 11. Other requirements
Requerimientos no cubiertos en ninguna otra sección del documento de requerimientos de software, por ejemplo: Requerimientos de bases de datos, internacionalización, legales y objetivos de reúso de componentes de software.

## 12. Glossary

* **UAT**: User Acceptance Testing
