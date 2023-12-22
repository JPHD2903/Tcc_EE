#FROM nginxinc/nginx-unprivileged
FROM nginx:1.21-alpine

# Timezone do container, utilizado nas mensagens de log
ENV TZ=America/Sao_Paulo

# Copia templates de configuração do nginx
#COPY --chown=nginx:nginx ./compose/nginx/default.conf.template /etc/nginx/templates/
COPY ./compose/nginx/default.conf.template /etc/nginx/templates/

#USER nginx