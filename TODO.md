What we have to do
==================

 * Add code to daemonize under Unix (http://www.jejik.com/articles/2007/02/a_simple_unix_linux_daemon_in_python/)
 * Move code to a package
 * Add a setup script
 * Use a database for bot configuration
    * Use [peewee](https://github.com/coleifer/peewee) to access this database
 * Make the bot able to load multiple bot configurations from the database and run them all in threads
 * add a small web interface (password protected) to access logs from the web
