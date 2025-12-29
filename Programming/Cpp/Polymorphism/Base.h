//
// Created by wolfy on 2/17/2025.
//

#ifndef CPP_BASE_H
#define CPP_BASE_H


class Base {
public:
    Base();

    virtual ~Base();

public:
    int _BaseVal;

    virtual void BaseFun1Virtual();
};


#endif //CPP_BASE_H
