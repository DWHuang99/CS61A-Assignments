CREATE TABLE parents AS
  SELECT "ace" AS parent, "bella" AS child UNION
  SELECT "ace"          , "charlie"        UNION
  SELECT "daisy"        , "hank"           UNION
  SELECT "finn"         , "ace"            UNION
  SELECT "finn"         , "daisy"          UNION
  SELECT "finn"         , "ginger"         UNION
  SELECT "ellie"        , "finn";

CREATE TABLE dogs AS
  SELECT "ace" AS name, "long" AS fur, 26 AS height UNION
  SELECT "bella"      , "short"      , 52           UNION
  SELECT "charlie"    , "long"       , 47           UNION
  SELECT "daisy"      , "long"       , 46           UNION
  SELECT "ellie"      , "short"      , 35           UNION
  SELECT "finn"       , "curly"      , 32           UNION
  SELECT "ginger"     , "short"      , 28           UNION
  SELECT "hank"       , "curly"      , 31;

CREATE TABLE sizes AS
  SELECT "toy" AS size, 24 AS min, 28 AS max UNION
  SELECT "mini"       , 28       , 35        UNION
  SELECT "medium"     , 35       , 45        UNION
  SELECT "standard"   , 45       , 60;


-- All dogs with parents ordered by decreasing height of their parent
CREATE TABLE by_parent_height AS
  SELECT a.child as name from parents as a,dogs as b where a.parent = b.name order by b.height desc;


-- The size of each dog
CREATE TABLE size_of_dogs AS
  SELECT a.name as name , b.size as size from dogs as a,sizes as b  where  a.height > b.min and a.height <= b.max ;


-- [Optional] Filling out this helper table is recommended
CREATE TABLE siblings AS
  SELECT a.child as brother ,b.child as sister from parents as a,parents as b where a.parent = b.parent and a.child < b.child order by a.child asc;

-- Sentences about siblings that are the same size
CREATE TABLE sentences AS
  SELECT concat('The two siblings, ',a.brother,' and ',a.sister,' have the same size: ',b.size) from siblings as a,size_of_dogs as b,size_of_dogs as c where a.brother = b.name and a.sister = c.name and b.size = c.size order by a.brother desc;


-- Height range for each fur type where all of the heights differ by no more than 30% from the average height
CREATE TABLE low_variance AS
SELECT
    fur,
    MAX(height) - MIN(height) AS height_range
FROM dogs
GROUP BY fur
HAVING MIN(height) >= AVG(height) * 0.7
   AND MAX(height) <= AVG(height) * 1.3;

