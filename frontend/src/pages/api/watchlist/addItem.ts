import {NextApiRequest, NextApiResponse} from 'next';
import { axiosBackendWithoutUser } from 'utils/axios';


// ----------------------------------------------------------------------

export default async (req: NextApiRequest, res: NextApiResponse) => {
    const {method} = req;

    if (method !== 'POST') {
        res.status(404).end();
    }

    const {watchlist_id, stock} = req.body

    try {
        const response = await axiosBackendWithoutUser.post(`api/watchlist/${watchlist_id}/items/`, {"stock": stock});
        const {id} = response.data;

        res.status(200).json(id);
    } catch (error) {
        res.status(500).end();
    }
}