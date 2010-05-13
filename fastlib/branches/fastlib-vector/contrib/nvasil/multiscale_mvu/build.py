librule(name="multiscale_mvu",
    headers=["multiscale_mvu.h"],
    deplibs=["fastlib:fastlib", "../all_centroid_knn:allcent",
    "../l_bfgs:l_bfgs", "../mvu:mvu"]
    );

binrule(name="test",
		sources=["multiscale_mvu_test.cc"],
    deplibs=[":multiscale_mvu"])
