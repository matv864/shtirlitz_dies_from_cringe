--
-- PostgreSQL database dump
--

-- Dumped from database version 16.2 (Debian 16.2-1.pgdg120+2)
-- Dumped by pg_dump version 16.2 (Debian 16.2-1.pgdg120+2)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: auth; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.joke (
    id integer NOT NULL,
    title character varying,
    theme character varying,
    text_joke text NOT NULL,
    creating date
);


ALTER TABLE public.joke OWNER TO postgres;

--
-- Name: joke_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.joke_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.joke_id_seq OWNER TO postgres;

--
-- Name: joke_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.joke_id_seq OWNED BY public.joke.id;


--
-- Name: joke id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.joke ALTER COLUMN id SET DEFAULT nextval('public.joke_id_seq'::regclass);


--
-- Data for Name: joke; Type: TABLE DATA; Schema: public; Owner: postgres
--

-- INSERT public.joke (id, title, theme, text_joke, creating) FROM stdin;
-- "1, TITLE_JOKE, THEME_JOKE, ХОРОШАЯ_ШУТКА, 2000-01-01"
-- \.
INSERT INTO public.joke (id, title, theme, text_joke, creating) 
VALUES (1, 'TITLE_JOKE', 'THEME_JOKE', 'ХОРОШАЯ_ШУТКА', '2000-01-01');


--
-- Name: joke_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.joke_id_seq', 1, true);


--
-- Name: joke joke_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.joke
    ADD CONSTRAINT joke_pk PRIMARY KEY (id);


--
-- PostgreSQL database dump complete
--