# Practical_task_5.7
## 1. Установка и настройка Docker и Docker Compose
### Установка Docker
Обновление индекса пакетов  
[_sudo apt-get update_](Pix/p_1_1.png)  
Установка необходимых пакетов  
[_sudo apt-get install ca-certificates curl gnupg_](Pix/p_1_2.png)  
Добавление официального GPG-ключа в Docker  
[_sudo install -m 0755 -d /etc/apt/keyrings curl -fsSL https://download.docker.com/linux/ubuntu/gpg |  
sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg   
sudo chmod a+r /etc/apt/keyrings/docker.gpg_](Pix/p_1_3.png)  
Добавление репозитория Docker в источники Apt и обновление индекса пакетов  
[_echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update_](Pix/p_1_4.png)
Установка пакетов Docker  
[_sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin_](Pix/p_1_5.png)  
Проверка установки  
[_sudo docker run hello-world_](Pix/p_1_6.png)  
### Установка Docker Compose
Загрузка исполняемого файла  
[_sudo curl -SL https://github.com/docker/compose/releases/download/v2.24.0/docker-compose-linux-x86_64 -o /usr/local/bin/docker-compose_][compose_link]  
Установка прав на исполнение для файла docker-compose  
[_sudo chmod +x /usr/local/bin/docker-compose_][compose_link]  
Проверка установки  
[_docker-compose --version_][compose_link]  

[compose_link]: Pix/p_1_9.png

### Настройка Docker для работы без прав root
Создание группы docker  
[_sudo groupadd docker_][no_sudo_link]  
Добавление пользователя в группу docker  
[_sudo usermod -aG docker $USER_][no_sudo_link]  
Активация изменений  
[_newgrp docker_][no_sudo_link]  
Проверка работы docker без sudo  
[_docker run hello-world_][no_sudo_link]

[no_sudo_link]: Pix/p_1_10.png

## 2. Разработка простой программы
Клонирован репозиторий на локальный компьютер  
[_git clone https://github.com/mvv-gthb/Practical_task_5.7_](Pix/p_2_1.png)  
Добавлен файл _ceaser.py_, реализующий шифр Цезаря  
Изменения отправлены в удаленный репозиторий  
[_git push_](Pix/p_2_2.png)  
