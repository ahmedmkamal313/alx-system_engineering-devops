# This script fix an issue in wordpress file

class wordpress::fix_wp_settings {
  file_line { 'replace-phpp-with-php-in-wp-settings':
    path  => '/var/www/html/wp-settings.php',
    line  => 'require_once(ABSPATH . \'wp-settings.php\');',
    match => 'phpp',
  }
}
