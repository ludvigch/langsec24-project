/**
 * This is an automatically generated file
 * @name Hello world
 * @kind problem
 * @problem.severity warning
 * @id python/example/hello-world
 */

import python

from Value len, CallNode call
where len.getName() = "setattr" and len.getACall() = call
select call, "A call to setattr"