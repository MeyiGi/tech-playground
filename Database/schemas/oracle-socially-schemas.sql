-- backend/init.sql

CREATE TABLE users (
    id VARCHAR2(36) PRIMARY KEY NOT NULL,
    email VARCHAR2(255) UNIQUE NOT NULL,
    username VARCHAR2(255) UNIQUE NOT NULL,
    password_hash VARCHAR2(255) NOT NULL,
    name VARCHAR2(255),
    bio VARCHAR2(1000),
    image VARCHAR2(1000),
    location VARCHAR2(255),
    website VARCHAR2(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE posts (
    id VARCHAR2(36) PRIMARY KEY NOT NULL,
    author_id VARCHAR2(36) NOT NULL,
    content CLOB,
    image VARCHAR2(1000),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_post_author FOREIGN KEY (author_id) REFERENCES users(id) ON DELETE CASCADE
);

CREATE TABLE comments (
    id VARCHAR2(36) PRIMARY KEY NOT NULL,
    content CLOB NOT NULL,
    author_id VARCHAR2(36) NOT NULL,
    post_id VARCHAR2(36) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_comment_author FOREIGN KEY (author_id) REFERENCES users(id) ON DELETE CASCADE,
    CONSTRAINT fk_comment_post FOREIGN KEY (post_id) REFERENCES posts(id) ON DELETE CASCADE
);

CREATE TABLE likes (
    id VARCHAR2(36) PRIMARY KEY NOT NULL,
    post_id VARCHAR2(36) NOT NULL,
    user_id VARCHAR2(36) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_like_user FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    CONSTRAINT fk_like_post FOREIGN KEY (post_id) REFERENCES posts(id) ON DELETE CASCADE,
    CONSTRAINT uq_like_user_post UNIQUE (user_id, post_id)
);

CREATE TABLE follows (
    follower_id VARCHAR2(36) NOT NULL,
    following_id VARCHAR2(36) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (follower_id, following_id),
    CONSTRAINT fk_follow_follower FOREIGN KEY (follower_id) REFERENCES users(id) ON DELETE CASCADE,
    CONSTRAINT fk_follow_following FOREIGN KEY (following_id) REFERENCES users(id) ON DELETE CASCADE
);

CREATE TABLE notifications (
    id VARCHAR2(36) PRIMARY KEY NOT NULL,
    user_id VARCHAR2(36) NOT NULL,
    creator_id VARCHAR2(36) NOT NULL,
    type VARCHAR2(20) NOT NULL,
    read_status NUMBER(1) DEFAULT 0,
    post_id VARCHAR2(36),
    comment_id VARCHAR2(36),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_notif_user FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    CONSTRAINT fk_notif_creator FOREIGN KEY (creator_id) REFERENCES users(id) ON DELETE CASCADE,
    CONSTRAINT fk_notif_post FOREIGN KEY (post_id) REFERENCES posts(id) ON DELETE CASCADE,
    CONSTRAINT fk_notif_comment FOREIGN KEY (comment_id) REFERENCES comments(id) ON DELETE CASCADE
);

COMMIT;