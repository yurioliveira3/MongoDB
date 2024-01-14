-- Show all databases
    show dbs

-- Change or Create a Database
    use blog -- use and name of db 

-- Create colletion 
    db.createCollection("posts")

    db.posts.insertOne(object)

-- insertOne()
    db.posts.insertOne({
        title: "Post Title 1",
        body: "Body of post.",
        category: "News",
        likes: 1,
        tags: ["news", "events"],
        date: Date()
    })

-- insertMany()
    db.posts.insertMany([  
        {
            title: "Post Title 2",
            body: "Body of post.",
            category: "Event",
            likes: 2,
            tags: ["news", "events"],
            date: Date()
        },
        {
            title: "Post Title 3",
            body: "Body of post.",
            category: "Technology",
            likes: 3,
            tags: ["news", "events"],
            date: Date()
        },
        {
            title: "Post Title 4",
            body: "Body of post.",
            category: "Event",
            likes: 4,
            tags: ["news", "events"],
            date: Date()
        }
    ])

-- find()
    db.posts.find() -- If left empty, all documents will be returned.

-- findOne()
    db.posts.findOne() -- It will return the first document it finds.

-- Querying Data
    -- db.posts.find( {category: "News"} )

    -- db.posts.find({}, {title: 1, date: 1}) -- This example will only display the title and date fields in the results.             

    -- db.posts.find({}, {_id: 0, title: 1, date: 1}) -- Exclude the _id field.
        -- We use a 1 to include a field and 0 to exclude a field.
    
    -- db.posts.find({}, {category: 0}) -- Exclude the date category field. All other fields will be included in the results.

    -- db.posts.find({}, {title: 1, date: 0}) -- We will get an error if we try to specify both 0 and 1 in the same object.

-- Update Document
    -- updateOne() -- update the first document that is found matching the provided query

    -- db.posts.find( { title: "Post Title 1" } )  -- Find the object

    -- db.posts.updateOne( { title: "Post Title 1" }, { $set: { likes: 2 } } )  -- Update object finded, set likes property to 2

    -- db.posts.find( { title: "Post Title 1" } ) -- Fint objetc after update 

-- Insert if not found
    -- If you would like to insert the document if it is not found, you can use the upsert option.
    db.posts.updateOne( 
        { title: "Post Title 5" }, 
        {
            $set: 
            {
                title: "Post Title 5",
                body: "Body of post.",
                category: "Event",
                likes: 5,
                tags: ["news", "events"],
                date: Date()
            }
        }, 
        { upsert: true }
    )

-- updateMany()
    -- db.posts.updateMany({}, { $inc: { likes: 1 } }) -- Update likes on all documents by 1. For this we will use the $inc (increment) operator

-- Delete Documents
    --  deleteOne()
        -- db.posts.deleteOne({ title: "Post Title 5" })
        -- method will delete the first document that matches the query provided.

    -- deleteMany()
        -- db.posts.deleteMany({ category: "Technology" })
        -- method will delete all documents that match the query provided.


Query Operators
There are many query operators that can be used to compare and reference document fields.

    * Comparison - Used in queries to compare values:
        $eq: Values are equal
        $ne: Values are not equal
        $gt: Value is greater than another value
        $gte: Value is greater than or equal to another value
        $lt: Value is less than another value
        $lte: Value is less than or equal to another value
        $in: Value is matched within an array
    
    * Logical - Logically compare multiple queries:
        $and: Returns documents where both queries match
        $or: Returns documents where either query matches
        $nor: Returns documents where both queries fail to match
        $not: Returns documents where the query does not match
        
    * Evaluation - Assist in evaluating documents:
        $regex: Allows the use of regular expressions when evaluating field values
        $text: Performs a text search
        $where: Uses a JavaScript expression to match documents
    
Update Operators
    Fields - The following operators can be used to update fields:
        $currentDate: Sets the field value to the current date
        $inc: Increments the field value
        $rename: Renames the field
        $set: Sets the value of a field
        $unset: Removes the field from the document
    
    Array - The following operators assist with updating arrays.
        $addToSet: Adds distinct elements to an array
        $pop: Removes the first or last element of an array
        $pull: Removes all elements from an array that match the query
        $push: Adds an element to an array

Aggregation Pipelines
    Aggregation operations allow you to group, sort, perform calculations, analyze data, and much more.

    db.posts.aggregate([
        // Stage 1: Only find documents that have more than 1 like
        {
            $match: { likes: { $gt: 1 } }
        },
        // Stage 2: Group documents by category and sum each categories likes
        {
            $group: { _id: "$category", totalLikes: { $sum: "$likes" } }
        }
    ])

    - $group = Group BY

        db.listingsAndReviews.aggregate(
            [ { $group : { _id : "$property_type" } } ]
        )

    - $limit = LIMIT

        db.movies.aggregate(
            [ { $limit: 1 } ]
        )

    - $project = SELECT + WHERE + LIMIT
        - We use a 1 to include a field and 0 to exclude a field.
        db.restaurants.aggregate([
            {
                $project: {
                    "name": 1,
                    "cuisine": 1,
                    "address": 1
                }
            },
            {
                $limit: 5
            }
        ])

    - $sort = ORDER BY 
        - The sort order can be chosen by using 1 or -1. 1 is ascending and -1 is descending.
        db.listingsAndReviews.aggregate([ 
            { 
                $sort: { "accommodates": -1 } 
            },
            {
                $project: {
                "name": 1,
                "accommodates": 1
                }
            },
            {
                $limit: 5
            }
        ])

    - $match = WHERE 
        - Behaves like a find.Filter documents that match the query provided.
        db.listingsAndReviews.aggregate([ 
            { 
                $match : { property_type : "House" } 
            },
            { 
                $limit: 2 
            },
            { 
                $project: {
                    "name": 1,
                    "bedrooms": 1,
                    "price": 1
                }
            }
        ])

    - $addFields = Calculated field

        db.restaurants.aggregate([
            {
                $addFields: {
                    avgGrade: { 
                        $avg: "$grades.score" 
                    }
                }
            },
            {
                $project: {
                    "name": 1,
                    "avgGrade": 1
                }
            },
            {
                $limit: 5
            }
        ])
    
    - $count = COUNT(0)
        db.restaurants.aggregate([
            {
                $match: { 
                    "cuisine": "Chinese"
                }
            },
            {
                $count: "totalChinese" = AS 
            }
        ])

    - $lookup = LEFT JOIN
        - Performs a left outer join to a collection in the same database.
            - from: The collection to use for lookup in the same database
            - localField: The field in the primary collection that can be used as a unique identifier in the from collection.
            - foreignField: The field in the from collection that can be used as a unique identifier in the primary collection.
            - as: The name of the new field that will contain the matching documents from the from collection.

        db.comments.aggregate([
            {
                $lookup: {
                    from: "movies",
                    localField: "movie_id",
                    foreignField: "_id",
                    as: "movie_details",
                },
            },
            {
                $limit: 1
            }
        ])

    - $out = INSERT INTO (...) SELECT (...) FROM (...)
        - This aggregation stage writes the returned documents from the aggregation pipeline to a collection.
        - The $out stage must be the last stage of the aggregation pipeline.

        db.listingsAndReviews.aggregate([
            {
                $group: {
                _id: "$property_type",
                properties: {
                        $push: {
                        name: "$name",
                        accommodates: "$accommodates",
                        price: "$price",
                    },
                },
                },
            },
            { 
                $out: "properties_by_type" 
            },
        ])

Indexing & Search
    - https://www.mongodb.com/basics/database-index

    1. From the Atlas dashboard, click on your Cluster name then the Search tab.
    2. Click on the Create Search Index button.
    3. Use the Visual Editor and click Next.
    4. Name your index, choose the Database and Collection you want to index and click Next.
        - If you name your index "default" you will not have to specify the index name in the $search pipeline stage.
        - Choose the sample_mflix database and the movies collection.
    5. Click Create Search Index and wait for the index to complete.

    - To use our search index, we will use the $search operator in our aggregation pipeline.

    db.movies.aggregate([
        {
            $search: {
                index: "default", // optional unless you named your index something other than "default"
                text: {
                    query: "star wars",
                    path: "title"
                },
            },
        },
        {
            $project: {
                title: 1,
                year: 1,
            }
        }
    ])

Schema Validation
    - By default MongoDB has a flexible schema. This means that there is no strict schema validation set up initially.
    - Schema validation rules can be created in order to ensure that all documents a collection share a similar structure.

    - MongoDB supports JSON Schema validation. The $jsonSchema operator allows us to define our document structure.

    db.createCollection("posts", {
        validator: {
            $jsonSchema: {
                bsonType: "object",
                required: [ "title", "body" ],
                properties: {
                    title: {
                        bsonType: "string",
                        description: "Title of post - Required."
                    },
                    body: {
                        bsonType: "string",
                        description: "Body of post - Required."
                    },
                    category: {
                        bsonType: "string",
                        description: "Category of post - Optional."
                    },
                    likes: {
                        bsonType: "int",
                        description: "Post like count. Must be an integer - Optional."
                    },
                    tags: {
                        bsonType: ["string"],
                        description: "Must be an array of strings - Optional."
                    },
                    date: {
                        bsonType: "date",
                        description: "Must be a date - Optional."
                    }
                }
            }
        }
    })

Data API Endpoints
    URL Endpoint example: 

    curl --location --request POST 'https://data.mongodb-api.com/app/<DATA API APP ID>/endpoint/data/v1/action/findOne' \
    --header 'Content-Type: application/json' \
    --header 'Access-Control-Request-Headers: *' \
    --header 'api-key: <DATA API KEY>' \
    --data-raw '{ 
        "dataSource":"<CLUSTER NAME>",
        "database":"sample_mflix",
        "collection":"movies",
        "projection": {"title": 1}
    }'