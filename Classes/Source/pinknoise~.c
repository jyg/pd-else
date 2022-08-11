// matt barber and porres (2018)
// based on SuperCollider's PinkNoise UGen

#include "m_pd.h"
#include "random.h"

#define PINK_DEF_HZ 40
#define PINK_MAX_OCT 31

static t_class *pinknoise_class;

typedef struct _pinknoise{
    t_object        x_obj;
    float           x_signals[PINK_MAX_OCT];
    float           x_total;
    int             x_octaves;
    int             x_octaves_set; // flag for if octaves to be set at dsp time
    t_random_state  x_rstate;
    t_outlet       *x_outlet;
}t_pinknoise;

static unsigned int instanc_n = 0;

static void pinknoise_init(t_pinknoise *x){
    int octaves = x->x_octaves;
    float *signals = x->x_signals;
    float total = 0;
    t_random_state *rstate = &x->x_rstate;
    uint32_t *s1 = &rstate->s1;
    uint32_t *s2 = &rstate->s2;
    uint32_t *s3 = &rstate->s3;
    for(int i = 0; i < octaves; ++i){
        float newrand = (random_frand(s1, s2, s3));
        total += newrand;
        signals[i] = newrand;
    }
    x->x_total = total;
}

static void pink_seed(t_pinknoise *x, t_symbol *s, int ac, t_atom *av){
    s = NULL;
    x->x_total = 0;
    unsigned int timeval;
    if(ac && av->a_type == A_FLOAT)
        timeval = (unsigned int)(atom_getfloat(av));
    else
        timeval = (unsigned int)(time(NULL)*151*++instanc_n);
    random_init(&x->x_rstate, timeval);
    pinknoise_init(x);
}

static void pink_oct(t_pinknoise *x, t_floatarg f){
    int octaves = (int)f;
    octaves = octaves < 0 ? 0 : octaves;
    octaves = octaves > PINK_MAX_OCT ? PINK_MAX_OCT : octaves;
    x->x_octaves = octaves;
    x->x_octaves_set = 0;
    pinknoise_init(x);
}

static void pinknoise_updatesr(t_pinknoise *x, t_float sr){
	int octaves = 0;
	while(sr > PINK_DEF_HZ){
		sr *= 0.5;
		octaves++;
	}
	x->x_octaves = octaves;
	pinknoise_init(x);
}

static t_int *pinknoise_perform(t_int *w){
    t_pinknoise *x = (t_pinknoise *)(w[1]);
    int n = (t_int)(w[2]);
    t_random_state *rstate = (t_random_state *)(w[3]);
    float *signals = (float*)(w[4]);
    t_sample *out = (t_sample *)(w[5]);
    int octaves = x->x_octaves;
    float total = x->x_total;
    uint32_t *s1 = &rstate->s1;
    uint32_t *s2 = &rstate->s2;
    uint32_t *s3 = &rstate->s3;
    while(n--){
    	uint32_t rcounter = random_trand(s1, s2, s3);
    	float newrand = random_frand(s1, s2, s3);
    	int k = (CLZ(rcounter));
    	if(k < octaves){
    		float prevrand = signals[k];
    		signals[k] = newrand;
    		total += (newrand - prevrand);
    	}
    	newrand = (random_frand(s1, s2, s3));
    	*out++ = (t_float)(total+newrand)/(octaves+1);
	}
	x->x_total = total;
    return(w+6);
}

static void pinknoise_dsp(t_pinknoise *x, t_signal **sp){
    if(x->x_octaves_set)
        pinknoise_updatesr(x, sp[0]->s_sr);
    dsp_add(pinknoise_perform, 5, x, sp[0]->s_n, &x->x_rstate, &x->x_signals, sp[0]->s_vec);
}

static void *pinknoise_new(t_symbol *s, int ac, t_atom *av){
    t_pinknoise *x = (t_pinknoise *)pd_new(pinknoise_class);
    x->x_outlet = outlet_new(&x->x_obj, &s_signal);
    inlet_new(&x->x_obj, &x->x_obj.ob_pd, &s_float, gensym("oct"));
    pink_seed(x, s, ac, av);
    if(ac > 1 && av[1].a_type == A_FLOAT)
    	pink_oct(x, atom_getfloatarg(1, ac, av));
    else
    	x->x_octaves_set = 1;
    return(x);
}

void pinknoise_tilde_setup(void){
    pinknoise_class = class_new(gensym("pinknoise~"), (t_newmethod)pinknoise_new,
        0, sizeof(t_pinknoise), 0, A_GIMME, 0);
    class_addmethod(pinknoise_class, (t_method)pinknoise_dsp, gensym("dsp"), A_CANT, 0);
    class_addmethod(pinknoise_class, (t_method)pink_seed, gensym("seed"), A_GIMME, 0);
    class_addmethod(pinknoise_class, (t_method)pink_oct, gensym("oct"), A_FLOAT, 0);
}
