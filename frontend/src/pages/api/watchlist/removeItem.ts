import {NextApiRequest, NextApiResponse} from 'next';
import { axiosBackendWithoutUser } from 'utils/axios';


// ----------------------------------------------------------------------

export default async (req: NextApiRequest, res: NextApiResponse) => {
    const {method} = req;

    if (method !== 'DELETE') {
        res.status(404).end();
    }

    const { watchlist_id, item_id } = req.query;

    try {
        const response = await axiosBackendWithoutUser.delete(`api/watchlist/${watchlist_id}/items/${item_id}/`);
        res.status(200).json(response.data);
    } catch (error) {
        res.status(500).end();
    }
}