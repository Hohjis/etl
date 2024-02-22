-- PostgreSQL SQL Dump
-- Version: 14

--
-- Database: 'etl'
--

-- --------------------------------------------------------

--
-- Table's estructure of table 'artists'
--

CREATE TABLE artists (
    id INTEGER,
    name TEXT,
    genres TEXT[],
    followers INTEGER,
    popularity INTEGER
);