-- Table: public.Region

CREATE TABLE IF NOT EXISTS region
(
    regname text COLLATE pg_catalog."default" NOT NULL,
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
    areaname text COLLATE pg_catalog."default" NOT NULL,
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
    languagename text COLLATE pg_catalog."default" NOT NULL,
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
    classprofilename text COLLATE pg_catalog."default" NOT NULL,
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
    name text COLLATE pg_catalog."default" NOT NULL,
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
    parentname text COLLATE pg_catalog."default" NOT NULL,
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
    name text COLLATE pg_catalog."default" NOT NULL,
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
    typename text COLLATE pg_catalog."default" NOT NULL,
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
    name text COLLATE pg_catalog."default" NOT NULL,
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
    name text COLLATE pg_catalog."default" NOT NULL,
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
    name text COLLATE pg_catalog."default" NOT NULL,
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
    outid character varying(100)[] COLLATE pg_catalog."default" NOT NULL,
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
    studentid character varying(100)[] COLLATE pg_catalog."default" NOT NULL,
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
    OWNER to postgres;