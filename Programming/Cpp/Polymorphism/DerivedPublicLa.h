//
// Created by wolfy on 2/17/2025.
//

#ifndef CPPREVIEW_DERIVEDPUBLICLA_H
#define CPPREVIEW_DERIVEDPUBLICLA_H


#include "Base.h"

class DerivedPublicLa : public Base {
public:
    DerivedPublicLa();

    ~DerivedPublicLa();

private:
    int _DerivedLaVal;
public:

    void BaseFun1Virtual();

};


#endif //CPPREVIEW_DERIVEDPUBLICLA_H
