class optimizer_config:
    def __init__(self):
        # optimizer config
        self.max_grad_norm = 5
        self.batch_size = 128
        self.train_batch_size = 128
        self.dev_batch_size = 128
        self.bucket_size_factor = 10
        self.DataParallel = False
        self.num_workers = 6
        self.weight_decay = 1e-2
        self.lr = 1e-3
        self.epochs = 50
        self.early_stop_patience = 10
        self.scheduler = "ReduceLROnPlateau"
        self.scheduler_patience = 2
        self.scheduler_reduce_factor = 0.5
        self.optimizer = "Ranger"
        self.save_by = "accuracy"
        self.metric_direction = 1
        self.different_betas = False
        self.chunk_size = -1
        self.display_metric = "accuracy"
        self.greedy_training = False


class base_config(optimizer_config):
    def __init__(self):
        super().__init__()
        self.word_embd_freeze = True
        self.initial_transform = True
        self.batch_pair = True
        self.embd_dim = 300
        self.input_size = 300
        self.hidden_size = 300
        self.classifier_hidden_size = 300
        self.global_state_only = True
        self.global_state_return = True
        self.parse_trees = False


class BiRecurrentGRC_config(base_config):
    def __init__(self):
        super().__init__()
        self.in_dropout = 0.4
        self.dropout = 0.1
        self.out_dropout = 0.1
        self.bidirectional = True
        self.encoder_type = "RecurrentGRC"
        self.model_name = "(BiRecurrentGRC)"

class BalancedTreeGRC_config(BiRecurrentGRC_config):
    def __init__(self):
        super().__init__()
        self.encoder_type = "BalancedTreeCell"
        self.model_name = "(BalancedTreeGRC)"



class EBT_GRC_config(BiRecurrentGRC_config):
    def __init__(self):
        super().__init__()
        self.stochastic = True
        self.beam_size = 5
        self.encoder_type = "EBT_GRC"
        self.model_name = "(EBT-GRC)"


class BT_GRC_config(BiRecurrentGRC_config):
    def __init__(self):
        super().__init__()
        self.stochastic = True
        self.beam_size = 5
        self.train_batch_size = 32
        self.encoder_type = "BT_GRC"
        self.model_name = "(BT-GRC)"

class BT_GRC_OS_config(BiRecurrentGRC_config):
    def __init__(self):
        super().__init__()
        self.stochastic = True
        self.beam_size = 5
        self.train_batch_size = 16
        self.encoder_type = "BT_GRC_OS"
        self.model_name = "(BT-GRC_OS)"


class CRvNN_config(BiRecurrentGRC_config):
    def __init__(self):
        super().__init__()
        self.train_batch_size = 32
        self.dev_batch_size = 64
        self.encoder_type = "CRvNN"
        self.model_name = "(CRvNN)"

class OM_config(BiRecurrentGRC_config):
    def __init__(self):
        super().__init__()
        self.dropout = 0.1
        self.memory_dropout = 0.1
        self.in_dropout = 0.4
        self.out_dropout = 0.1
        self.memory_slots = 12
        self.encoder_type = "OrderedMemory"
        self.model_name = "(OM)"

class HEBT_GRC_config(BiRecurrentGRC_config):
    def __init__(self):
        super().__init__()
        self.stochastic = True
        self.norm = "skip"
        self.s4_dropout = self.dropout
        self.pre_SSM = True
        self.rba_temp = 1
        self.prenorm = False
        self.beam_size = 7
        self.model_chunk_size = 30
        self.RBA = True
        self.RBA_random = False
        self.RBA_advanced = False
        self.encoder_type = "HEBT_GRC"
        self.model_name = "(HEBT_GRC)"

class HGRC_config(HEBT_GRC_config):
    def __init__(self):
        super().__init__()
        self.encoder_type = "HGRC"
        self.model_name = "(HGRC)"

class HEBT_GRC_noSSM_config(HEBT_GRC_config):
    def __init__(self):
        super().__init__()
        self.pre_SSM = False
        self.encoder_type = "HEBT_GRC"
        self.model_name = "(HEBT_GRC_noSSM)"


class GAU_IN_config(EBT_GRC_config):
    def __init__(self):
        super().__init__()
        self.encoder_type = "GAU_IN"
        self.model_name = "(GAU-IN)"

class EBT_GAU_IN_config(EBT_GRC_config):
    def __init__(self):
        super().__init__()
        self.encoder_type = "EBT_GAU_IN"
        self.model_name = "(EBT-GAU-IN)"


class EGT_GAU_IN_config(EBT_GRC_config):
    def __init__(self):
        super().__init__()
        self.encoder_type = "EGT_GAU_IN"
        self.model_name = "(EGT-GAU-IN)"

class EGT_GRC_config(BiRecurrentGRC_config):
    def __init__(self):
        super().__init__()
        self.encoder_type = "EGT_GRC"
        self.model_name = "(EGT-GRC)"

class SadsNetWork_config(HEBT_GRC_config):
    def __init__(self):
        super().__init__()
        self.encoder_type = "SadsNetWork"
        self.model_name = "(SadsNetWork)"
        self.taskName = "QQP"
        self.isBatchFirst = True
        self.isNeedHidden = False
        self.isBiDirectional = True
        self.trainDataNum = 100
        self.trainDataDim = self.input_size
        self.lobeLabelDim = self.input_size
        self.labelDataDim = self.input_size
        self.hiddenDim = 300
        self.layerNum = 1
        self.maxSeqLen = 30
        self.splitPartNum = 25
        self.crossLenRate = 0.01
        self.maxLevelNum = 6
        self.cacheSize = 4
        self.maxLoopCount = 1
        self.manualSeed = 42
        self.resDropRate = 0.1
        self.batchSize = self.batch_size * 2
        self.learnRate = 1e-3
        self.weightDecay = 1e-2

class MambaNetWork_config(HEBT_GRC_config):
    def __init__(self):
        super().__init__()
        self.encoder_type = "MambaNetWork"
        self.model_name = "(MambaNetWork)"
        self.taskName = "QQP"
        self.isBatchFirst = True
        self.isNeedHidden = False
        self.isBiDirectional = True
        self.trainDataNum = 100
        self.trainDataDim = self.input_size
        self.lobeLabelDim = self.input_size
        self.labelDataDim = self.input_size
        self.hiddenDim = 10
        self.layerNum = 1
        self.kernelSize = 3
        self.padNum = 1
        self.manualSeed = 42
        self.resDropRate = 0.05
        self.batchSize = self.batch_size
        self.learnRate = 1e-3
        self.weightDecay = 1e-8


