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
    id TEXT PRIMARY KEY,
    name TEXT,
    genres TEXT[],
    followers INTEGER,
    popularity INTEGER
);