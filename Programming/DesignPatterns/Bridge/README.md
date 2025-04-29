# Bridge Design Pattern

A bridge desing pattern connects components together through abstraction to reduce the complexity of the code structure.

A use case of bridge design pattern is when we have different features that can be applied to different objects.

Instead of writing classes for each feature x object, which will end up with (number of features) x (number of objects) different classes, we can build a bridge between features and objects, so we only need to make one class for each feature, one class for each object, and a bridge class to connect the feature and object.
