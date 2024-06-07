import styles from './Check.list.page.module.scss';
import { Page } from '@shared/ui';
import { CardLink } from '@shared/ui/card';
import { CheckList } from '@features/check.list';

export default function CheckListPage() {
	return (
		<Page title="Чек-листы">
			<CheckList />
			<CardLink
				title="Получи награду за выполнение уровня"
				className={styles.rewart_trio}
			/>
		</Page>
	);
}
