create_normal_form_tables = """-- Table: public.Region

CREATE TABLE IF NOT EXISTS region
(
    regname text COLLATE pg_catalog."default",
    CONSTRAINT "Region_pkey" PRIMARY KEY (regname)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE region
    OWNER to postgres;
----------------------------------------------------------------------
-- Table: public.Area

CREATE TABLE IF NOT EXISTS area
(
    areaname text COLLATE pg_catalog."default",
    regname text COLLATE pg_catalog."default",
    CONSTRAINT "Area_pkey" PRIMARY KEY (areaname),
    CONSTRAINT "RegNameFK" FOREIGN KEY (regname)
        REFERENCES region (regname) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE area
    OWNER to postgres;
----------------------------------------------------------------------

-- Table: public.ClassLang

CREATE TABLE IF NOT EXISTS classlang
(
    languagename text COLLATE pg_catalog."default",
    CONSTRAINT "ClassLang_pkey" PRIMARY KEY (languagename)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE classlang
    OWNER to postgres;
----------------------------------------------------------------------

-- Table: public.ClassProfile

CREATE TABLE IF NOT EXISTS classprofile
(
    classprofilename text COLLATE pg_catalog."default",
    CONSTRAINT "ClassProfile_pkey" PRIMARY KEY (classprofilename)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE classprofile
    OWNER to postgres;
----------------------------------------------------------------------
-- Table: public.DPALevel

CREATE TABLE IF NOT EXISTS dpalevel
(
    name text COLLATE pg_catalog."default",
    CONSTRAINT "DPALevel_pkey" PRIMARY KEY (name)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE dpalevel
    OWNER to postgres;
----------------------------------------------------------------------
-- Table: public.ParentSchool

CREATE TABLE IF NOT EXISTS parentschool
(
    parentname text COLLATE pg_catalog."default",
    CONSTRAINT "ParentSchool_pkey" PRIMARY KEY (parentname)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE parentschool
    OWNER to postgres;
----------------------------------------------------------------------

-- Table: public.Registration

CREATE TABLE IF NOT EXISTS registration
(
    name text COLLATE pg_catalog."default",
    CONSTRAINT "RegistrationName_pkey" PRIMARY KEY (name)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE registration
    OWNER to postgres;
----------------------------------------------------------------------

-- Table: public.SchoolType

CREATE TABLE IF NOT EXISTS schooltype
(
    typename text COLLATE pg_catalog."default",
    CONSTRAINT "SchoolType_pkey" PRIMARY KEY (typename)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE schooltype
    OWNER to postgres;
----------------------------------------------------------------------

-- Table: public.StudentGender

CREATE TABLE IF NOT EXISTS studentgender
(
    name text COLLATE pg_catalog."default",
    CONSTRAINT "StudentGender_pkey" PRIMARY KEY (name)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE studentgender
    OWNER to postgres;
----------------------------------------------------------------------

-- Table: public.TeritoryType

CREATE TABLE IF NOT EXISTS teritorytype
(
    name text COLLATE pg_catalog."default",
    CONSTRAINT "TeritoryType_pkey" PRIMARY KEY (name)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE teritorytype
    OWNER to postgres;
----------------------------------------------------------------------

-- Table: public.Teritory

CREATE TABLE IF NOT EXISTS teritory
(
    name text COLLATE pg_catalog."default",
    tertype text COLLATE pg_catalog."default",
    areaname text COLLATE pg_catalog."default",
    CONSTRAINT "Teritory_pkey" PRIMARY KEY (name),
    CONSTRAINT "TerAreaFk" FOREIGN KEY (areaname)
        REFERENCES area (areaname) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT "TerTypeFk" FOREIGN KEY (tertype)
        REFERENCES teritorytype (name) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE teritory
    OWNER to postgres;
----------------------------------------------------------------------

-- Table: public.SchoolDetails

CREATE TABLE IF NOT EXISTS schooldetails
(
    schoolname text COLLATE pg_catalog."default" NOT NULL,
    schooltype text COLLATE pg_catalog."default",
    schoolparent text COLLATE pg_catalog."default",
    CONSTRAINT "SchoolDetails_pkey" PRIMARY KEY (schoolname),
    CONSTRAINT "SchoolDetailsTypeFk" FOREIGN KEY (schooltype)
        REFERENCES schooltype (typename) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT "SchoolParentFk" FOREIGN KEY (schoolparent)
        REFERENCES parentschool (parentname) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE schooldetails
    OWNER to postgres;
----------------------------------------------------------------------

-- Table: public.School

CREATE TABLE IF NOT EXISTS school
(
    name text COLLATE pg_catalog."default" NOT NULL,
    teritory text COLLATE pg_catalog."default",
    CONSTRAINT "School_pkey" PRIMARY KEY (name),
    CONSTRAINT "SchoolTeritoryFK" FOREIGN KEY (teritory)
        REFERENCES teritory (name) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE school
    OWNER to postgres;
----------------------------------------------------------------------

-- Table: public.TestStatus

CREATE TABLE IF NOT EXISTS teststatus
(
    name text COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT "TestStatus_pkey" PRIMARY KEY (name)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE teststatus
    OWNER to postgres;
----------------------------------------------------------------------

-- Table: public.TestSubject

CREATE TABLE IF NOT EXISTS testsubject
(
    subject text COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT "Test_pkey" PRIMARY KEY (subject)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE testsubject
    OWNER to postgres;
----------------------------------------------------------------------

-- Table: public.Testyear_no

CREATE TABLE IF NOT EXISTS testyear
(
    year_no smallint NOT NULL,
    CONSTRAINT "Testyear_no_pkey" PRIMARY KEY (year_no)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE testyear
    OWNER to postgres;
----------------------------------------------------------------------

-- Table: public.TestLanguage

CREATE TABLE IF NOT EXISTS testlanguage
(
    languagename text NOT NULL,
    CONSTRAINT "Testlang_pkey" PRIMARY KEY (languagename)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE testlanguage
    OWNER to postgres;
----------------------------------------------------------------------
-- Table: public.Student

CREATE TABLE IF NOT EXISTS student
(
    outid text COLLATE pg_catalog."default" NOT NULL,
    birthday smallint,
    gender text COLLATE pg_catalog."default",
    teritoryname text COLLATE pg_catalog."default",
    classprofilename text COLLATE pg_catalog."default",
    classlangname text COLLATE pg_catalog."default",
    school text COLLATE pg_catalog."default",
    registrationname text COLLATE pg_catalog."default",
    CONSTRAINT "Student_pkey" PRIMARY KEY (outid),
    CONSTRAINT "CProfileStidentFk" FOREIGN KEY (classprofilename)
        REFERENCES classprofile (classprofilename) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT "classlangnamefk" FOREIGN KEY (classlangname)
        REFERENCES classlang (languagename) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT "RegistrTypeFk" FOREIGN KEY (registrationname)
        REFERENCES registration (name) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT "SchoolStudentFk" FOREIGN KEY (school)
        REFERENCES school (name) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT "StudentGenderFk" FOREIGN KEY (gender)
        REFERENCES studentgender (name) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT "TerStudentFk" FOREIGN KEY (teritoryname)
        REFERENCES teritory (name) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE student
    OWNER to postgres;

----------------------------------------------------------------------
-- Table: public.Test

CREATE TABLE IF NOT EXISTS test
(
    studentid text COLLATE pg_catalog."default" NOT NULL,
    subject text COLLATE pg_catalog."default" NOT NULL,
    year_no smallint NOT NULL,
	testlanguage text COLLATE pg_catalog."default",
    status text COLLATE pg_catalog."default",
    ball100 numeric,
    ball12 numeric,
    ballTest numeric,
    apaptscale numeric,
    dpalevel text COLLATE pg_catalog."default",
    school text COLLATE pg_catalog."default",
    CONSTRAINT "Test_pkey1" PRIMARY KEY (studentid, subject, "year_no"),
    CONSTRAINT "StudentTestFk" FOREIGN KEY (studentid)
        REFERENCES student (outid) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT "TestDPAFk" FOREIGN KEY (dpalevel)
        REFERENCES dpalevel (name) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT "TestSchoolFk" FOREIGN KEY (school)
        REFERENCES school (name) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT "TestStatusFk" FOREIGN KEY (status)
        REFERENCES teststatus (name) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT "TestSubjectFk" FOREIGN KEY (subject)
        REFERENCES testsubject (subject) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT "Testyear_noFk" FOREIGN KEY ("year_no")
        REFERENCES testyear (year_no) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
	CONSTRAINT "TestLangFk" FOREIGN KEY (testlanguage)
        REFERENCES testlanguage (languagename) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE test
    OWNER to postgres;"""
    
delete_tables = """DROP TABLE IF EXISTS region CASCADE;

DROP TABLE IF EXISTS area CASCADE;

DROP TABLE IF EXISTS classlang CASCADE;

DROP TABLE IF EXISTS classprofile CASCADE;

DROP TABLE IF EXISTS dpalevel CASCADE;

DROP TABLE IF EXISTS parentschool CASCADE;

DROP TABLE IF EXISTS registration CASCADE;

DROP TABLE IF EXISTS schooltype CASCADE;

DROP TABLE IF EXISTS studentgender CASCADE;

DROP TABLE IF EXISTS teritorytype CASCADE;

DROP TABLE IF EXISTS teritory CASCADE;

DROP TABLE IF EXISTS schooldetails CASCADE;

DROP TABLE IF EXISTS school CASCADE;

DROP TABLE IF EXISTS teststatus CASCADE;

DROP TABLE IF EXISTS testsubject CASCADE;

DROP TABLE IF EXISTS testyear CASCADE;

DROP TABLE IF EXISTS testlanguage CASCADE;

DROP TABLE IF EXISTS student CASCADE;

DROP TABLE IF EXISTS test CASCADE;"""

migrate_data_in_db = """insert into region(regname)
select distinct 
	case
		when regname is NULL then 'Невідомо'
		else regname
	end from znodata
	on conflict do nothing;

insert into area(areaname,regname)
select distinct
	case
		when areaname is NULL then 'Невідомо'
		else areaname
	end,
	regname
	from znodata
on conflict do nothing;

insert into teritorytype(Name)
select distinct 
	case
		when tertypename is NULL then 'Невідомо'
		else tertypename
	end from znodata
on conflict do nothing;

insert into teritory(name,tertype,areaname)
select distinct tername,tertypename,areaname from znodata
on conflict do nothing;
----------------------------------------------------------------------
insert into schooltype(typename) 
select distinct
	case
		when eotypename is NULL then 'Невідомо'
		else eotypename
	end from znodata
on conflict do nothing;

insert into parentschool(parentname) 
select distinct
	case
		when eoparent is NULL then 'Невідомо'
		else eoparent
	end from znodata
on conflict do nothing;

INSERT INTO schooldetails (schoolname, schooltype, schoolparent)
select distinct
	case
		when eoname is NULL then '№154'
		else eoname
	end,
	eotypename,
	eoparent from znodata
	on conflict do nothing;

INSERT INTO school (name, teritory)
select distinct
	case
		when eoname is NULL then '№154'
		else eoname
	end,
	tername from znodata
	union all
	select distinct
	case
		when ukrptname is NULL then '№154'
		else ukrptname
	end,
	ukrpttername from znodata
	union all
	select distinct
	case
		when histptname is NULL then '№154'
		else histptname
	end,
	histpttername from znodata
	union all
	select distinct
	case
		when mathptname is NULL then '№154'
		else mathptname
	end,
	mathpttername from znodata
	union all
	select distinct
	case
		when physptname is NULL then '№154'
		else physptname
	end,
	physpttername from znodata
	union all
	select distinct
	case
		when chemptname is NULL then '№154'
		else chemptname
	end,
	chempttername from znodata
	union all
	select distinct
	case
		when bioptname is NULL then '№154'
		else bioptname
	end,
	biopttername from znodata
	union all
	select distinct
	case
		when geoptname is NULL then '№154'
		else geoptname
	end,
	geopttername from znodata
	union all
	select distinct
	case
		when engptname is NULL then '№154'
		else engptname
	end,
	engpttername from znodata
	union all
	select distinct
	case
		when fraptname is NULL then '№154'
		else fraptname
	end,
	frapttername from znodata
	union all
	select distinct
	case
		when deuptname is NULL then '№154'
		else deuptname
	end,
	deupttername from znodata
	union all
	select distinct
	case
		when spaptname is NULL then '№154'
		else spaptname
	end,
	spapttername from znodata
	on conflict do nothing;
----------------------------------------------------------------------

insert into registration(name)
select distinct 
	case
		when regtypename is NULL then 'Невідомо'
		else regtypename
	end from znodata
on conflict do nothing;

insert into classprofile(classprofilename)
select distinct 
	case
		when classprofilename is NULL then 'Невідомо'
		else classprofilename
	end from znodata
on conflict do nothing;


insert into classlang(languagename)
select distinct
	case
		when classlangname is NULL then 'Невідомо'
		else classlangname
	end from znodata
on conflict do nothing;


insert into studentgender(name)
select distinct
	case
		when sextypename is NULL then 'Невідомо'
		else sextypename
	end from znodata
on conflict do nothing;

INSERT INTO student (outid, birthday, gender, teritoryname, classprofilename, classlangname, school, registrationname) 
select distinct 
	outid,
	birth,
	sextypename,
	tername,
	classprofilename,
	classlangname,
	eoname,
	regtypename	from znodata
	on conflict do nothing;
----------------------------------------------------------------------

INSERT INTO testsubject(subject)
values
('Українська мова і література')
,('Історія України')
,('Математика')
,('Фізика')
,('Хімія')
,('Географія')
,('Французька мова')
,('Німецька мова')
,('Іспанська мова')
,('Біологія')
,('Англійська мова')
on conflict do nothing;

insert into testyear(year_no) 
select distinct
	case
		when year is NULL then 0
		else year
	end from znodata
on conflict do nothing;

insert into teststatus(name) 
select distinct
	case
		when mathteststatus is NULL then 'Невідомо'
		else mathteststatus
	end from znodata
on conflict do nothing;

insert into dpalevel(name) 
select distinct
	case
		when engdpalevel is NULL then 'Невідомо'
		else engdpalevel
	end
	from znodata

	union all

	select distinct
		case
			when fradpalevel is NULL then 'Невідомо'
			else fradpalevel
		end
	from znodata

	union all

	select distinct
		case
			when deudpalevel is NULL then 'Невідомо'
			else deudpalevel
		end
	from znodata
	
	union all

	select distinct
		case
			when spadpalevel is NULL then 'Невідомо'
			else spadpalevel
		end
	from znodata
	on conflict do nothing;

insert into testlanguage 
select distinct
	case
		when histlang is NULL then 'Невідомо'
		else histlang
	end
	from znodata

	union all

	select distinct
		case
			when mathlang is NULL then 'Невідомо'
			else mathlang
		end
	from znodata

	union all

	select distinct
		case
			when physlang is NULL then 'Невідомо'
			else physlang
		end
	from znodata
	on conflict do nothing;


INSERT INTO test (studentid, subject, year_no,  status, ball100, ball12, balltest, apaptscale, school) 
select 
	outid, ukrtest,year, ukrteststatus, ukrball100, ukrball12, ukrball, cast(ukradaptscale as numeric), ukrptname from znodata
	where ukrtest notnull
	on conflict do nothing;
	
INSERT INTO test (studentid, subject, year_no, testlanguage, status, ball100, ball12, balltest, school) 
select 
	outid, histtest, year,histlang, histteststatus, histball100, histball12, histball, histptname from znodata
	where histtest notnull
	on conflict do nothing;
	
INSERT INTO test (studentid, subject, year_no, testlanguage, status, ball100, ball12, balltest, school) 
select 
	outid, mathtest, year, mathlang, mathteststatus, mathball100, mathball12, mathball, mathptname from znodata
	where mathtest notnull
	on conflict do nothing;
	
INSERT INTO test (studentid, subject, year_no, testlanguage, status, ball100, ball12, balltest, school) 
select 
	outid, phystest, year, physlang, physteststatus, physball100, physball12, physball, physptname from znodata
	where phystest notnull
	on conflict do nothing;
	
INSERT INTO test (studentid, subject, year_no, testlanguage, status, ball100, ball12, balltest, school) 
select 
	outid, chemtest, year, chemlang, chemteststatus, chemball100, chemball12, chemball, chemptname from znodata
	where chemtest notnull
	on conflict do nothing;

INSERT INTO test (studentid, subject, year_no, testlanguage, status, ball100, ball12, balltest, school) 
select 
	outid, biotest, year, biolang, bioteststatus, bioball100, bioball12, bioball, bioptname from znodata
	where biotest notnull
	on conflict do nothing;

INSERT INTO test (studentid, subject, year_no, testlanguage, status, ball100, ball12, balltest, school) 
select 
	outid, geotest, year, geolang, geoteststatus, geoball100, geoball12, geoball, geoptname from znodata
	where geotest notnull
	on conflict do nothing;

INSERT INTO test (studentid, subject, year_no, status, ball100, ball12, balltest, dpalevel, school) 
select 
	outid, engtest, year,  engteststatus, engball100, engball12, engball, engdpalevel, engptname from znodata
	where engtest notnull
	on conflict do nothing;
	
INSERT INTO test (studentid, subject, year_no, status, ball100, ball12, balltest, dpalevel, school) 
select 
	outid, fratest, year,  frateststatus, fraball100, fraball12, fraball, fradpalevel, fraptname from znodata
	where fratest notnull
	on conflict do nothing;
	
INSERT INTO test (studentid, subject, year_no, status, ball100, ball12, balltest, dpalevel, school) 
select 
	outid, deutest, year,  deuteststatus, deuball100, deuball12, deuball, deudpalevel, deuptname from znodata
	where deutest notnull
	on conflict do nothing;

INSERT INTO test (studentid, subject, year_no, status, ball100, ball12, balltest, dpalevel, school) 
select 
	outid, spatest, year,  spateststatus, spaball100, spaball12, spaball, spadpalevel, spaptname from znodata
	where spatest notnull
	on conflict do nothing;
----------------------------------------------------------------------
"""

query = """select max(Ball100) as "Results", year_no as "Year"
  FROM public.test WHERE status = 'Зараховано' AND year_no IN (2019, 2020)
  GROUP BY year_no
  ORDER BY year_no;"""