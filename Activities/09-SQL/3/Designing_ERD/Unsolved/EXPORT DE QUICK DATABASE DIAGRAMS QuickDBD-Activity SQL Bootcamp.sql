-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- Link to schema: https://app.quickdatabasediagrams.com/#/d/NhlWzL
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.

-- Modify this code to update the DB schema diagram.
-- To reset the sample schema, replace everything with
-- two dots ('..' - without quotes).

drop table "Trainers";

CREATE TABLE "Trainers" (
    "TrainerID" int   NOT NULL,
    "Trainer_first_Name" VARCHAR   NOT NULL,
    "Trainer_last_Name" VARCHAR   NOT NULL,
    "CustomerID" int   NOT NULL,
    CONSTRAINT "pk_Trainers" PRIMARY KEY (
        "TrainerID"
     )
);

select * from "Trainers";

CREATE TABLE "Members" (
    "CustomerID" int   NOT NULL,
    "customer_first_Name" VARCHAR   NOT NULL,
    "customer_last_Name" VARCHAR   NOT NULL,
    "cust_address" varchar   NOT NULL,
    "cust_city" varchar   NOT NULL,
    "gymID" int   NOT NULL,
    "TrainerID" int   NOT NULL,
    "PayID" int   NOT NULL,
    CONSTRAINT "pk_Members" PRIMARY KEY (
        "CustomerID"
     )
);

CREATE TABLE "Gym" (
    "GymID" int   NOT NULL,
    "gymname" varchar   NOT NULL,
    "address" varchar   NOT NULL,
    "city" varchar   NOT NULL,
    "zipcode" varchar   NOT NULL,
    "TrainerID" int   NOT NULL,
    "CustomerID" int   NOT NULL,
    CONSTRAINT "pk_Gym" PRIMARY KEY (
        "GymID"
     )
);

CREATE TABLE "Payments" (
    "PayID" int   NOT NULL,
    "creditcard" int   NOT NULL,
    "billing_zip" int   NOT NULL,
    CONSTRAINT "pk_Payments" PRIMARY KEY (
        "PayID"
     )
);

ALTER TABLE "Trainers" ADD CONSTRAINT "fk_Trainers_CustomerID" FOREIGN KEY("CustomerID")
REFERENCES "Members" ("CustomerID");

ALTER TABLE "Members" ADD CONSTRAINT "fk_Members_gymID" FOREIGN KEY("gymID")
REFERENCES "Gym" ("GymID");

ALTER TABLE "Members" ADD CONSTRAINT "fk_Members_TrainerID" FOREIGN KEY("TrainerID")
REFERENCES "Trainers" ("TrainerID");

ALTER TABLE "Members" ADD CONSTRAINT "fk_Members_PayID" FOREIGN KEY("PayID")
REFERENCES "Payments" ("PayID");

ALTER TABLE "Gym" ADD CONSTRAINT "fk_Gym_TrainerID" FOREIGN KEY("TrainerID")
REFERENCES "Trainers" ("TrainerID");

ALTER TABLE "Gym" ADD CONSTRAINT "fk_Gym_CustomerID" FOREIGN KEY("CustomerID")
REFERENCES "Members" ("CustomerID");

