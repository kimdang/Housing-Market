
import execute_mysql

analysis_figure_query = "CREATE TABLE analysis_figure (count INT AUTO_INCREMENT PRIMARY KEY, historical_url VARCHAR(255), pct_change_url VARCHAR(255), predict_url VARCHAR(255), location_id INT, FOREIGN KEY (location_id) REFERENCES location(id) ON UPDATE CASCADE)"
execute_mysql.run_query(analysis_figure_query)
print('analysis_figure table created.')

analysis_val_query = "CREATE TABLE analysis_value (count INT AUTO_INCREMENT PRIMARY KEY, pct_avg FLOAT(6,2), std FLOAT(6,2), five_year FLOAT(6,2), ten_year FLOAT(6,2), location_id INT, FOREIGN KEY (location_id) REFERENCES location(id) ON UPDATE CASCADE)"
execute_mysql.run_query(analysis_val_query)
print('analysis_value table created.')

