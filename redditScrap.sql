CREATE TABLE ft_posts (
	post_key INTEGER PRIMARY KEY NOT NULL,
	post_id varchar2(100) NOT NULL,
	date_key INTEGER NOT NULL,
	sub_id varchar2(10) NOT NULL,
	post_title varchar(100) NOT NULL,
	post_body blob default NULL,
	post_score varchar2(100) NOT NULL,
	postRS number default 0,
	com_num INTEGER NOT NULL,
	FOREIGN KEY (date_key) REFERENCES dd_dates(date_key),
	FOREIGN KEY (sub_id) REFERENCES dd_subreddits(sub_id)
);

CREATE TABLE dd_subreddits (
	sub_id varchar2(10) PRIMARY KEY NOT NULL,
	name varchar2(30) NOT NULL,
	title varchar2(50) NOT NULL	
);

CREATE TABLE ft_comments (
	com_key INTEGER PRIMARY KEY NOT NULL,
	com_id INTEGER NOT NULL,
	date_key INTEGER NOT NULL,
	post_id varchar2(10) NOT NULL,
	sub_id varchar2(10) NOT NULL,
	com_body blob default NULL,
	com_score INTEGER not NULL,
	FOREIGN KEY (date_key) REFERENCES dd_dates(date_key),
	FOREIGN KEY (post_id) REFERENCES ft_posts(post_id),
	FOREIGN KEY (sub_id) REFERENCES dd_subreddits(sub_id)
);

CREATE TABLE ft_subRS (
	subRS_key INTEGER PRIMARY KEY NOT NULL,
	date_key INTEGER NOT NULL,
	sub_id varchar2(10) NOT NULL,
	subRS number default 0,
	FOREIGN KEY (date_key) REFERENCES dd_dates(date_key),
	FOREIGN KEY (sub_id) REFERENCES dd_subreddits(sub_id)
);

CREATE TABLE dd_dates (
	date_key INTEGER PRIMARY KEY NOT NULL,
	run_date DATETIME NOT NULL,
	seq INTEGER NOT NULL
);