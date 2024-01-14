# Practical_task_5.7
## 1. Установка и настройка Docker и Docker Compose
[_sudo apt-get update_](https://github.com/mvv-gthb/Practical_task_5.7/blob/main/p_1_1.png) - обновление индекса пакетов  
[_sudo apt-get install ca-certificates curl gnupg](https://github.com/mvv-gthb/Practical_task_5.7/blob/main/p_1_2.png) - установка необходимых пакетов  
[sudo install -m 0755 -d /etc/apt/keyrings curl -fsSL https://download.docker.com/linux/ubuntu/gpg |  
sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg   
sudo chmod a+r /etc/apt/keyrings/docker.gpg](https://github.com/mvv-gthb/Practical_task_5.7/blob/main/p_1_3.png) - добавление официального GPG-ключа в Docker
