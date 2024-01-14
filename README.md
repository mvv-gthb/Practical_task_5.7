# Practical_task_5.7
## 1. Установка и настройка Docker и Docker Compose
Обновление индекса пакетов  
[_sudo apt-get update_](https://github.com/mvv-gthb/Practical_task_5.7/blob/main/p_1_1.png)  
Установка необходимых пакетов  
[_sudo apt-get install ca-certificates curl gnupg_](https://github.com/mvv-gthb/Practical_task_5.7/blob/main/p_1_2.png)  
Добавление официального GPG-ключа в Docker  
[_sudo install -m 0755 -d /etc/apt/keyrings curl -fsSL https://download.docker.com/linux/ubuntu/gpg |  
sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg   
sudo chmod a+r /etc/apt/keyrings/docker.gpg_](https://github.com/mvv-gthb/Practical_task_5.7/blob/main/p_1_3.png)  
Добавление репозитория Docker в источники Apt и обновление индекса пакетов  
[_echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update_](p_1_4.png)

