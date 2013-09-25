[![Build Status](https://travis-ci.org/omnidan/simple-code-generator.png?branch=master)](https://travis-ci.org/omnidan/simple-code-generator)

Basic syntax
============

Simple Model File (SMF) - Structure
-----------------------------------
    (model|class|struct) <modelname>:
        <type> <parameter>

Syntax types
------------
`model` sets the syntax type to the default model.

`struct` sets the syntax type to C-like-struct-model, which requires usage of semicolons and { }.

`class` is basically an alias for struct, but used in C++-like-class-models.

Later, there will be a library to use these C++ and C models in actual C/C++ code.

Optional parts of the style
---------------------------
Spacing, indentation, semicolon after parameter

Examples
--------
### Model (Simple)
    model School:
        string location
        int teacher_count
        int pupils_count

### Struct (C)
    struct School {
        string location;
        int teacher_count;
        int pupils_count;
    };
(should work in C when you define string)

### Class (C++)
    class School {
        string location;
        int teacher_count;
        int pupils_count;
    };
(should work in C++ when you specify `using namespace std;`)

Advanced syntax
===============

Arrays
------

### Structure
    <type> (array|list) <parameter>
    or
    (array|list) <type> <parameter>
    or
    []

### Optional parts of the style
Spacing

[] can be suffix/prefix of type or parameter

array must be prefix/suffix of the type

Instead of using the array or list, you can also append an "s" to the type. For example: Teachers loads an array of the model Teacher.

### Examples
#### Model (Simple)
    model School:
        string location
        string array teacher_names
        int pupils_count

#### Struct (C)
    struct School {
        string location;
        string teachers[];
        int pupils_count;
    };

#### Class (C++)
    struct School {
        string location;
        string teachers[];
        int pupils_count;
    };

Imports
-------
### Syntax
    import <modelname>

### Optional parts of the style
Semicolon after parameter, C/C++-like function

### Examples
#### Model (Simple)
    import Teacher
    model School:
        string location
        Teachers teachers
        int pupils_count

#### Struct (C)
    import("Teacher");
    struct School {
        string location;
        Teacher teachers[];
        int pupils_count;
    };

#### Class (C++)
    import("Teacher");
    struct School {
        string location;
        Teacher teachers[];
        int pupils_count;
    };
