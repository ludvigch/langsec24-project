/**
 * @name Hello world
 * @kind problem
 * @problem.severity warning
 * @id python/example/hello-world
 */

import python

predicate isRecursive(PythonFunctionValue f) {
    f.getACall().getScope() = f.getScope()
}

from PythonFunctionValue targetFunc
where isRecursive(targetFunc) 
select targetFunc, "recursive function"