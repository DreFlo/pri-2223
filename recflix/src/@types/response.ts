import type { Title } from './title';
import type { Credit } from './credit';

export type Response = {
    numFound: number;
    start: number;
    numFoundExact: boolean;
    docs: (Title | Credit)[];
};