-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- Link to schema: https://app.quickdatabasediagrams.com/#/d/Y5FiED
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.


CREATE TABLE "job_location" (
    "city" VARCHAR(25)   NOT NULL,
    "state" VARCHAR(25)   NOT NULL,
    "job_id" VARCHAR(15)   NOT NULL,
    CONSTRAINT "pk_job_location" PRIMARY KEY (
        "job_id"
     )
);

CREATE TABLE "skills_required" (
    "skills" VARCHAR(25)   NOT NULL,
    "job_title" VARCHAR(25)   NOT NULL,
    "job_id" varchar(25)   NOT NULL,
    CONSTRAINT "pk_skills_required" PRIMARY KEY (
        "job_id"
     )
);

CREATE TABLE "company" (
    "job_id" varchar(25)   NOT NULL,
    "company_name" varchar(25)   NOT NULL,
    "job_title" varchar(25)   NOT NULL,
    CONSTRAINT "pk_company" PRIMARY KEY (
        "job_id"
     )
);

CREATE TABLE "job_descriptions" (
    "job_id" varchar(25)   NOT NULL,
    "job_description" varchar(50)   NOT NULL,
    "job_title" varchar(25)   NOT NULL,
    CONSTRAINT "pk_job_descriptions" PRIMARY KEY (
        "job_id"
     )
);

ALTER TABLE "company" ADD CONSTRAINT "fk_company_job_title" FOREIGN KEY("job_title")
REFERENCES "skills_required" ("job_title");

ALTER TABLE "job_descriptions" ADD CONSTRAINT "fk_job_descriptions_job_title" FOREIGN KEY("job_title")
REFERENCES "company" ("job_title");

