insert into region(regname)
select distinct 
	case
		when regname is NULL then 'Невідомо'
		else regname
	end from znodata;

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

INSERT INTO school (schoolname, teritory)
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


insert into studentgender(gendername)
select distinct
	case
		when sextypename is NULL then 'Невідомо'
		else sextypename
	end from znodata
on conflict do nothing;

INSERT INTO students (outid, birth, gender, tername, classprofilename, classlangname, schol, registrationtypename) 
select distinct on (outid)
	case
		when outid is NULL then 'outid'
		else outid
	end,
	birth,
	sextypename,
	tername,
	classprofilename,
	classlangname,
	eoname,
	regtypename	from znodata;
----------------------------------------------------------------------

INSERT INTO testsubjext(subject)
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
,('Англійська мова');

insert into testyear(year) 
select distinct
	case
		when year is NULL then 'Невідомо'
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
	end from znodata
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
		when zp.mathlang is NULL then 'Невідомо'
		else zp.mathlang
	end
from znodata

union all

select distinct
	case
		when zp.physlang is NULL then 'Невідомо'
		else zp.physlang
	end
from znodata

on conflict do nothing;


INSERT INTO test (studentid, subject, year_no,  status, ball100, ball12, balltest, adaptscale, school) 
select 
	outid, ukrtest,year, ukrteststatus, ukrball100, ukrball12, ukrball, ukradaptscale, ukrptname from znodata as z1
	where ukrtest notnull;
	
INSERT INTO test (studentid, subject, year_no, testlanguage, status, ball100, ball12, balltest, school) 
select 
	outid, histtest, year,histlang, histteststatus, histball100, histball12, histball, histptname from znodata as z1
	where ukrtest notnull;
	
INSERT INTO test (studentid, subject, year_no, testlanguage, status, ball100, ball12, balltest, school) 
select 
	outid, mathtest, year, mathlang, mathteststatus, mathball100, mathball12, mathball, mathptname from znodata
	where mathtest notnull;
	
INSERT INTO test (studentid, subject, year_no, testlanguage, status, ball100, ball12, balltest, school) 
select 
	outid, phystest, year, physlang, physteststatus, physball100, physball12, physball, physptname from znodata
	where phystest notnull;
	
INSERT INTO test (studentid, subject, year_no, testlanguage, status, ball100, ball12, balltest, school) 
select 
	outid, chemtest, year, chemlang, chemteststatus, chemball100, chemball12, chemball, chemptname from znodata
	where chemtest notnull;

INSERT INTO test (studentid, subject, year_no, testlanguage, status, ball100, ball12, balltest, school) 
select 
	outid, biotest, year, biolang, bioteststatus, bioball100, bioball12, bioball, bioptname from znodata
	where biotest notnull;

INSERT INTO test (studentid, subject, year_no, testlanguage, status, ball100, ball12, balltest, school) 
select 
	outid, geotest, year, geolang, geoteststatus, geoball100, geoball12, geoball, geoptname from znodata
	where geotest notnull;

INSERT INTO test (studentid, subject, year_no, status, ball100, ball12, balltest, dpalevel, school) 
select 
	outid, engtest, year,  engteststatus, engball100, engball12, engball, engdpalevel, engptname from znodata
	where engtest notnull;
	
INSERT INTO test (studentid, subject, year_no, status, ball100, ball12, balltest, dpalevel, school) 
select 
	outid, fratest, year,  frateststatus, fraball100, fraball12, fraball, fradpalevel, fraptname from znodata
	where fratest notnull;
	
INSERT INTO test (studentid, subject, year_no, status, ball100, ball12, balltest, dpalevel, school) 
select 
	outid, deutest, year,  deuteststatus, deuball100, deuball12, deuball, deudpalevel, deuptname from znodata
	where deutest notnull;

INSERT INTO test (studentid, subject, year_no, status, ball100, ball12, balltest, dpalevel, school) 
select 
	outid, spatest, year,  spateststatus, spaball100, spaball12, spaball, spadpalevel, spaptname from znodata
	where spatest notnull;
----------------------------------------------------------------------


