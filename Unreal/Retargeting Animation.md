# Retargeting Animation
1. Create IK Rig for both the targeting character and the wanted animation.

## Retargeting Animation from Mixamo
1. Download a character mesh and import it to Unreal, leave the Skeletal part to None since the skeletal is contained in the model
	1. ![[importModel1.png]]
2. We'll have a skeletal mesh and a skeleton asset after the import is done
3. Download the preferred animation from Mixamo, without the skin since we already downloaded the mesh. Then import it to the Unreal project with skeletal **selected** to the previously downloaded mesh.
	1. ![[importAnimation.png]]
 4. Create an **IKRig** asset from the skeletal mesh downloaded from Mixamo
	 1. Find the hips location and set it to root bone
		 1. ![[createIKRig1.png]]
	   2. Create chains with the names and set of bones same as the other IKRig (we created) for  the targeting character.
5. Create an **IK Retargeter** asset that maps the just created IKRig to the IKRig for the target skeletal mesh.