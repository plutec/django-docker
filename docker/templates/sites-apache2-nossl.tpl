<VirtualHost *:80>
        ServerName {{domain}}

        Alias /static /var/www/{{appname}}/static_files
        <Directory /var/www/{{appname}}/static_files>
                Require all granted
        </Directory>
        ServerAdmin name@{{domain}}
        
        #DocumentRoot /var/www/html
        
        <Directory /var/www/{{appname}}/{{appname}}>
                <Files wsgi.py>
                        Require all granted
                </Files>
        </Directory>

        WSGIProcessGroup {{appname}}
        WSGIScriptAlias / /var/www/{{appname}}/{{appname}}/wsgi.py
        WSGIApplicationGroup %{GLOBAL}

        ServerAdmin webmaster@localhost

        # Available loglevels: trace8, ..., trace1, debug, info, notice, warn,
        # error, crit, alert, emerg.
        # It is also possible to configure the loglevel for particular
        # modules, e.g.
        LogLevel error

        ErrorLog ${APACHE_LOG_DIR}/{{appname}}-nossl.error.log
        CustomLog ${APACHE_LOG_DIR}/{{appname}}-nossl.access.log combined

        # For most configuration files from conf-available/, which are
        # enabled or disabled at a global level, it is possible to
        # include a line for only one particular virtual host. For example the
        # following line enables the CGI configuration for this host only
        # after it has been globally disabled with "a2disconf".
        #Include conf-available/serve-cgi-bin.conf
        #RewriteEngine on
        #RewriteCond %{SERVER_NAME} =yarahub.com
        #RewriteRule ^ https://%{SERVER_NAME}%{REQUEST_URI} [END,QSA,R=permanent]
</VirtualHost>
