import torch

print("PyTorch version:", torch.__version__)
print("CUDA available:", torch.cuda.is_available())
print("CUDA device count:", torch.cuda.device_count())

# 检查是否有可用的GPU
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Running on device: {device}")

import omicverse as ov
import scanpy as sc
import scvelo as scv

ov.plot_set()


# Data preprocessed

adata = scv.datasets.pancreas()
#quantity control
adata=ov.pp.qc(
    adata,
    tresh={'mito_perc': 0.20, 'nUMIs': 500, 'detected_genes': 250},
    mt_startswith='mt-'
)
#normalize and high variable genes (HVGs) calculated
adata=ov.pp.preprocess(adata,mode='shiftlog|pearson',n_HVGs=2000,)
#save the whole genes and filter the non-HVGs
adata.raw = adata
adata = adata[:, adata.var.highly_variable_features]
#scale the adata.X
ov.pp.scale(adata)
#Dimensionality Reduction
ov.pp.pca(adata,layer='scaled',n_pcs=50)

# Constructing a metacellular object

meta_obj=ov.single.MetaCell(
    adata,
    use_rep='scaled|original|X_pca',
    n_metacells=None,
    use_gpu='cuda:0'
    # use_gpu=None # 设置为 None 表示使用 CPU
)
meta_obj.initialize_archetypes()

# Train and save the model

import time
s_time = time.time()
meta_obj.train(min_iter=10, max_iter=50)
print('=============> train timeout:', time.time() - s_time)
meta_obj.save('seacells/model.pkl')

# Predicted the metacells

meta_obj.load('seacells/model.pkl')
ad=meta_obj.predicted(method='soft',celltype_label='clusters',
                     summarize_layer='lognorm')

# Benchmarking

SEACell_purity = meta_obj.compute_celltype_purity('clusters')
separation = meta_obj.separation(use_rep='scaled|original|X_pca',nth_nbr=1)
compactness = meta_obj.compactness(use_rep='scaled|original|X_pca')

import seaborn as sns
import matplotlib.pyplot as plt
ov.plot_set()
fig, axes = plt.subplots(1,3,figsize=(4,4))
sns.boxplot(data=SEACell_purity, y='clusters_purity',ax=axes[0],
           color=ov.utils.blue_color[3])
sns.boxplot(data=compactness, y='compactness',ax=axes[1],
           color=ov.utils.blue_color[4])
sns.boxplot(data=separation, y='separation',ax=axes[2],
           color=ov.utils.blue_color[4])
plt.tight_layout()
plt.suptitle('Evaluate of MetaCells',fontsize=13,y=1.05)
for ax in axes:
    ax.grid(False)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(True)
    ax.spines['left'].set_visible(True)

import matplotlib.pyplot as plt
fig, ax = plt.subplots(figsize=(4,4))
ov.pl.embedding(
    meta_obj.adata,
    basis="X_umap",
    color=['clusters'],
    frameon='small',
    title="Meta cells",
    #legend_loc='on data',
    legend_fontsize=14,
    legend_fontoutline=2,
    size=10,
    ax=ax,
    alpha=0.2,
    #legend_loc='',
    add_outline=False,
    #add_outline=True,
    outline_color='black',
    outline_width=1,
    show=False,
    #palette=ov.utils.blue_color[:],
    #legend_fontweight='normal'
)
ov.single.plot_metacells(ax,meta_obj.adata,color='#CB3E35',
                                  )

# Get the raw obs value from adata

ov.single.get_obs_value(ad,adata,groupby='S_score',
                       type='mean')
ad.obs.head()

# Visualize the MetaCells

import scanpy as sc
ad.raw=ad.copy()
sc.pp.highly_variable_genes(ad, n_top_genes=2000, inplace=True)
ad=ad[:,ad.var.highly_variable]

ov.pp.scale(ad)
ov.pp.pca(ad,layer='scaled',n_pcs=30)
ov.pp.neighbors(ad, n_neighbors=15, n_pcs=20,
               use_rep='scaled|original|X_pca')

ov.pp.umap(ad)

ad.obs['celltype']=ad.obs['celltype'].astype('category')
ad.obs['celltype']=ad.obs['celltype'].cat.reorder_categories(adata.obs['clusters'].cat.categories)
ad.uns['celltype_colors']=adata.uns['clusters_colors']

ov.pl.embedding(ad, basis='X_umap',
                color=["celltype","S_score"],
                frameon='small',cmap='RdBu_r',
               wspace=0.5)
