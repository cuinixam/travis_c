static unsigned char light = 0;

void light_turn_on(void)
{
        light = 1;
}

void light_turn_off(void)
{
        light = 0;
}

unsigned char read_light(void)
{
        return light;
}
